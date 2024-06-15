from transformers import AutoTokenizer, AutoModel
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import torch
from torch.utils.data import DataLoader
from sklearn.cluster import MiniBatchKMeans, KMeans
from sklearn import metrics
from tqdm import tqdm
import os
from ast_research.utils import *
os.environ['TOKENIZERS_PARALLELISM'] = 'true'

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  # 设备

def encoding(model, tokenizer, sentences):
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

def K_cluster_analysis(K, X):
    mb_kmeans = KMeans(n_clusters=K, init="k-means++", n_init='auto')
    # mb_kmeans = MiniBatchKMeans(n_clusters=K, init="k-means++", n_init='auto') # KMeans在大数据量时速度较慢
    y_pred = mb_kmeans.fit_predict(X)
    CH_score = metrics.calinski_harabasz_score(X, y_pred)
    si_score = metrics.silhouette_score(X, y_pred)
    return y_pred, mb_kmeans.cluster_centers_ ,CH_score, si_score

def cluster_kmeans(sub_trees, cluster_range, output_path, code_num):    
    kmeans_data = pd.DataFrame(
        {
            "subtrees_txt": [x.ts_node.text for x in sub_trees],
            "subtrees_id": [x.subtree_id for x in sub_trees],
            "sub_trees": [str(x) for x in sub_trees],
            "subtrees_codeid": [x.code_id for x in sub_trees]
        }
    )
    tokenizer = AutoTokenizer.from_pretrained("/data/hf_cache/hub/models--bert-base-uncased", )
    model = AutoModel.from_pretrained("/data/hf_cache/hub/models--bert-base-uncased")
    subtrees_list = kmeans_data["sub_trees"].tolist()
    subtrees_vec = encoding(model, tokenizer, subtrees_list)
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

    return list(zip(subtrees_list, y_pred))




if __name__ == "__main__":
    pass
