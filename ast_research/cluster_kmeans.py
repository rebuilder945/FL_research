from transformers import AutoTokenizer, AutoModel
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
from torch.utils.data import DataLoader
from sklearn.cluster import MiniBatchKMeans, KMeans
from sklearn import metrics
from tqdm import tqdm
import networkx as nx
import os
from ast_research.utils import *
os.environ['TOKENIZERS_PARALLELISM'] = 'true'

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  # 设备

def bert_encoding(sentences):
    tokenizer = AutoTokenizer.from_pretrained("/data/hf_cache/hub/models--bert-base-uncased", )
    model = AutoModel.from_pretrained("/data/hf_cache/hub/models--bert-base-uncased")
    model.eval()
    model.to(device)
    max_char_len = 256
    sents_inputs = tokenizer(
        sentences,
        return_tensors="pt",
        max_length=max_char_len,
        padding="max_length",
        truncation=True,
    )
    input_ids = sents_inputs['input_ids']
    atten_vec = sents_inputs['attention_mask']
    tmp = list(zip(input_ids, atten_vec))
    dataloader = DataLoader(tmp, batch_size=128, shuffle=False)
    sents_vec = []
    tqdm_batch_iterator = tqdm(dataloader, desc='sentence encoding ')
    for index, batch in enumerate(tqdm_batch_iterator):
        input_ids, atten_vec = batch
        sents_vec.append(model(input_ids.to(device), attention_mask=atten_vec.to(device))['pooler_output'].detach().cpu().numpy().tolist())
    torch.cuda.empty_cache()
    sents_vec = [np.array(xi) for x in sents_vec for xi in x]
    return sents_vec

def get_all_nodes(root):
    ans = set()
    for child in root.children:
        ans.add(root.type)
        ans.add(child.type)
        ans.update(get_all_nodes(child))
    return ans

def getnodeandedge(node, src, tgt):
    for child in node.children:
        src.append(node.type)
        tgt.append(child.type)
        getnodeandedge(child, src, tgt)

def get_single_cent_matrix(tree_root, type2index: dict, g: nx.Graph):
    # 获取所有边
    src = []
    tgt = []
    getnodeandedge(tree_root, src, tgt)
    all_nodes = set(src + tgt)

    # 向图中加入所有边
    for i in range(len(src)):
        m = type2index[src[i]]
        n = type2index[tgt[i]]
        if g.has_edge(m, n):
            g[m][n]['weight'] += 1
        else:
            g.add_edge(m, n, weight=1)
    
    this_all_cents = dict()

    # try:
    this_all_cents["cent_harm"] = [cent /len(g) for cent in nx.harmonic_centrality(g).values()]
    this_all_cents["cent_eigen"] = [cent for cent in nx.eigenvector_centrality(g).values()]
    this_all_cents["cent_close"] = [cent for cent in nx.closeness_centrality(g).values()]
    this_all_cents["cent_between"] = [cent for cent in nx.betweenness_centrality(g).values()]
    this_all_cents["cent_degree"] = [cent for cent in nx.degree_centrality(g).values()]
    this_all_cents["cent_katz"] = [cent for cent in nx.katz_centrality(g).values()]
    # except:
    #     return

    res = []
    for x in this_all_cents.values():
        res += x

    return res

class CentEncoding:
    def __init__(self, sub_trees) -> None:
        self.g = nx.Graph()

        # 获取所有树的节点type，并编号
        all_types = set()
        for s in sub_trees:
            all_types.update(get_all_nodes(s.ts_node))
        self.type2index = {tp: index for index, tp in enumerate(all_types)}

        # 给图加入所有树的所有节点
        for tp, index in self.type2index.items():
            self.g.add_node(index, name = tp)

        self.tree_vecs = {}

        # 对每棵树进行编码
        for s in tqdm(sub_trees, total=len(sub_trees)):
            # 仅清除边，保证节点数量相等，每棵树的嵌入维度相等
            self.g.clear_edges()
            cent_matrix = get_single_cent_matrix(
                tree_root=s.ts_node,
                type2index=self.type2index,
                g=self.g
            )
            self.tree_vecs[s.subtree_id] = cent_matrix

    def sing_tree_encode(self, tree_root):
        return self.tree_vecs[tree_root.subtree_id]


def cent_encoding(sub_trees: list[SubTreeNode]):

    g = nx.Graph()

    # 获取所有树的节点type，并编号
    all_types = set()
    for s in sub_trees:
        all_types.update(get_all_nodes(s.ts_node))
    type2index = {tp : index for index, tp in enumerate(all_types)}

    # 给图加入所有树的所有节点
    for tp, index in type2index.items():
        g.add_node(index, name = tp)

    res = {}

    # 对每棵树进行编码
    for s in tqdm(sub_trees, total=len(sub_trees)):
        # 仅清除边，保证节点数量相等，每棵树的嵌入维度相等
        g.clear_edges()
        cent_matrix = get_single_cent_matrix(
            tree_root=s.ts_node,
            type2index=type2index,
            g=g
        )
        # print(cent_matrix)
    return res


def K_cluster_analysis(K, X):
    mb_kmeans = KMeans(n_clusters=K, init="k-means++", n_init='auto')
    # mb_kmeans = MiniBatchKMeans(n_clusters=K, init="k-means++", n_init='auto') # KMeans在大数据量时速度较慢
    y_pred = mb_kmeans.fit_predict(X)
    CH_score = metrics.calinski_harabasz_score(X, y_pred)
    si_score = metrics.silhouette_score(X, y_pred)
    return y_pred, mb_kmeans.cluster_centers_ ,CH_score, si_score

def cluster_kmeans(sub_trees, cluster_range, encoding_alg, output_path, code_num):    
    # TODO: 改进此处的效率
    kmeans_data = pd.DataFrame(
        {
            "subtrees_txt": [x.ts_node.text for x in sub_trees],
            "subtrees_id": [x.subtree_id for x in sub_trees],
            "sub_trees": [str(x) for x in sub_trees],
            "subtrees_codeid": [x.code_id for x in sub_trees]
        }
    )

    if encoding_alg == 'bert_encoding':
        # subtrees_list = kmeans_data["sub_trees"].tolist()
        subtrees_vec = bert_encoding(kmeans_data["sub_trees"].tolist())
    else:
        subtrees_vec = cent_encoding(sub_trees)

    bert_df = pd.DataFrame({"embedding": subtrees_vec})
    bert_features = pd.DataFrame(subtrees_vec)

    # 设置超参数（聚类数目K）搜索范围
    Ks = range(cluster_range[0], cluster_range[1])
    CH_scores = []
    si_scores = []
    score = 0
    y_pred = []
    Best_K = Ks[0]
    centers = None
    for K in tqdm(Ks, total=len(Ks), desc='cluster_kmeans...'):
        y_p, cen, ch, si = K_cluster_analysis(K, bert_features)
        CH_scores.append(ch)
        si_scores.append(si)
        if ch * si > score:
            score = ch * si
            Best_K = K
            y_pred = y_p
            centers = cen
    
    # 最佳超参数
    print("the best cluster find is {}".format(Best_K))
    
    # 绘制不同K对应的聚类的性能，找到最佳模型／参数（分数最高）
    plt.plot(Ks, np.array(CH_scores), 'b-', label='CH_scores')
    plt.savefig(os.path.join(output_path, "calinski_score.png"))
    plt.plot(Ks, np.array(si_scores), 'b-', label='si_scores')
    plt.savefig(os.path.join(output_path, "silhouette_score.png"))

    # 计算每一类的tf-idf值
    cls_dict = {}
    for pred_cls, sbt in zip(y_pred, sub_trees):
        if pred_cls not in cls_dict:
            cls_dict[pred_cls] = []
        cls_dict[pred_cls].append(sbt)
    cal_tfidf(cls_dict, sub_trees, code_num)

    # 绘制直方图
    histogram_draw(y_pred, Best_K, output_path)  

    # 绘制散点图
    draw_cluster(
        dataset=bert_features,
        centers=centers,
        sample_dim=len(bert_features.iloc[0, :]),
        cluster_num=Best_K,
        labels=y_pred,
        output_path=output_path,
    )

    # 保存聚类结果
    train_kmeans = pd.concat(
        [
            pd.Series(name="Kmeans_" + str(Best_K), data=y_pred),
            pd.Series(name="tf-idf value", data=[x.tfidf for x in sub_trees]),
            kmeans_data,
            bert_df
        ],
        axis=1,
    )
    train_kmeans.sort_values(by=["tf-idf value", "Kmeans_" + str(Best_K)], inplace=True, ascending=False)
    train_kmeans.to_csv(os.path.join(output_path, "count.csv"), index=False)

    # return list(zip(subtrees_list, y_pred))


if __name__ == "__main__":
    pass
