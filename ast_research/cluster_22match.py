import os
from tqdm import tqdm
from zss import simple_distance
from ast_research.utils import *

# kmeans
import time
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from numpy import nonzero, array
from sklearn.metrics import f1_score, accuracy_score, normalized_mutual_info_score, rand_score, adjusted_rand_score
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA

range_ = [6, 8]
dis_threshold = 1
cls_flag = True
src_path = rf'ast_research/out/ans_png_{range_[0]}_{range_[1]}-{dis_threshold}-True'

def cluster_22match(sub_trees: list[SubTreeNode], dis_threshold, output_path, code_num):
    ans = {} # {cls: [subtree]}
    cls_index = 0 # 目前最大的类别id，用于新增类
    flags = {} # 子树id：类别id
    cls_flags = {} # 类别id：类内子树数量
    for x in tqdm(range(len(sub_trees)), total=len(sub_trees), desc='cluster_22match...'):
        for y in range(x + 1, len(sub_trees)):
            id_x = id(sub_trees[x])
            id_y = id(sub_trees[y])            
            # 基于编辑距离归类
            if sub_trees[x].__eq__(
                value=sub_trees[y], 
                threshold=dis_threshold
            ):
                if cls_index not in cls_flags:
                    cls_flags[cls_index] = 0

                if id_x not in flags and id_y not in flags:
                    flags[id_x] = cls_index
                    flags[id_y] = cls_index
                    cls_flags[cls_index] += 2
                    cls_index += 1
                elif id_x in flags and id_y in flags:
                    continue
                elif id_x in flags and id_y not in flags:
                    flags[id_y] = flags[id_x]
                    cls_flags[cls_index] += 1
                else:
                    flags[id_x] = flags[id_y]
                    cls_flags[cls_index] += 1

                # count the cls
                if flags[id_x] not in ans:
                    ans[flags[id_x]] = set()
                ans[flags[id_x]].add(sub_trees[x])
                ans[flags[id_x]].add(sub_trees[y])
                sub_trees[x].type = flags[id_x]
                sub_trees[y].type = flags[id_x]

    # 处理未匹配到相似子树的离群点
    clsed_subtree_ids = []
    for cls, sb_s in ans.items():
        ans[cls] = list(sb_s)
        clsed_subtree_ids += [sb.subtree_id for sb in sb_s]
    print(f'valid_cls: {len(ans)}')
    un_clsed_subtree_num = 0
    for x in sub_trees:
        if x.subtree_id not in clsed_subtree_ids:
            ans[cls_index] = [x]
            cls_index += 1
            un_clsed_subtree_num += 1
    print(f'valid_cls_tree: {len(clsed_subtree_ids)}, outliers: {un_clsed_subtree_num}')

    # 计算tf-idf
    cal_tfidf(ans, sub_trees, code_num)
    
    # 绘制直方图
    hist_data = []
    for x, y in ans.items():
        hist_data += [x] * len(y)
    histogram_draw(hist_data, len(ans), output_path)
    
    # 保存聚类结果
    df = pd.DataFrame(
        {
            "subtrees_cls": [x.type for x in sub_trees],
            "tf-idf value": [x.tfidf for x in sub_trees],
            "subtrees_txt": [x.ts_node.text for x in sub_trees],
            "subtrees_id": [x.subtree_id for x in sub_trees],
            "sub_trees": [str(x) for x in sub_trees],
            "subtrees_codeid": [x.code_id for x in sub_trees],
        }
    )
    df.sort_values(by=["tf-idf value", "subtrees_cls"], inplace=True, ascending=False)
    df.to_csv(os.path.join(output_path, 'count.csv'), index=False)

    return ans



if __name__ == "__main__":
    pass