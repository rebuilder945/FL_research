import os
import sys
sys.path.append(os.getcwd())
import tree_sitter_python as tspython
from tree_sitter import Language, Parser
from ast_research.utils import *
from ast_research.cluster_22match import *
from ast_research.cluster_kmeans import *

# tree-sitter config
PY_Lang = Language(tspython.language())
py_parser = Parser()
py_parser.language = PY_Lang

# hyper-param config
depth_range = (5, 20) # 控制树的深度

cluster_range = (10, 50) # kmeans聚类中心范围
encoding_alg = "cent_encoding"
# encoding_alg = "bert_encoding"

dis_threshold = 0.1 # 树22匹配距离认为相似的阈值
dis_alg = "cent"
# dis_alg = "edit"

code_from = "ch_3004" # 程序来自哪些章节以及哪一题
cls_flag = False # 从错误还是正确的程序中进行聚类

# src code path
code_path = rf'/home/wdy/code_LLM/FL_research/ast_research/data/{code_from}/{cls_flag}'

# kmeans output path
kmeans_output_path = os.path.join(
    f"ast_research/out/kmeans_output/{encoding_alg}",
    code_from,
    f"{cls_flag}_{depth_range[0]}_{depth_range[1]}-{cluster_range[0]}-{cluster_range[1]}",
)
folder_check(kmeans_output_path)

# editDis + 22match output path
match22_ouput_path = os.path.join(
    f"ast_research/out/match22_ouput/",
    code_from,
    f"{cls_flag}_{depth_range[0]}_{depth_range[1]}-{dis_threshold}-{dis_alg}"
)
folder_check(match22_ouput_path)


def main():
    # 获取所有子树
    sub_trees = []
    code_num = len(os.listdir(code_path))
    for code_id, f in enumerate(os.listdir(code_path)):
        code_str = file_reader(os.path.join(code_path, f))
        code_tree = py_parser.parse(bytes(code_str, 'utf8'))
        sub_trees += get_all_subtrees(code_tree.root_node, depth_range, code_id)

    # 用github项目：tree2vec 试，不太行，其特征向量不连续
    # tmp_path = 'ex/tree2vec/tmp_tree'
    # folder_check(tmp_path)
    # for index, sub_tree in enumerate(sub_trees):
    #     with open(os.path.join(tmp_path, f'subTree_{index}.json'), 'w') as fp:
    #         json.dump(sub_tree, fp)

    # 子树编号
    for index, sub_tree in enumerate(sub_trees): 
        sub_tree.subtree_id = index
    print(f'{len(sub_trees)} sub_trees')
    
    # TODO: 6.24: 制作评估聚类效果的数据集

    # kmeans   
    # cluster_kmeans(
    #     sub_trees=sub_trees,
    #     cluster_range=cluster_range,
    #     encoding_alg=encoding_alg,
    #     output_path=kmeans_output_path,
    #     code_num=code_num,
    # )

    # editDis + 22match
    cluster_22match(
        sub_trees=sub_trees,
        dis_threshold=dis_threshold,
        output_path=match22_ouput_path,
        code_num=code_num,
    )

    # cent_matrix + kmeans
    

    print('done!')
    print(f'result saved to {match22_ouput_path}')


if __name__ == '__main__':
    main()
#     code_snippet = """
# a = int(input())
# b = int(input())
# if a > b:
#     print(a)
# else:
#     print(a)    
# """
    # code_ = 'for y in range(2,x,1):\n            if x%y==0:\n                break\n        else:\n            n2.append(x)'
    # code_ = 'for i in range(2,x): \n        if x%i==0:\n            break\n    else:\n            l2.append(x)'
#     code_ = \
# """
# for y in range(2,x,1):
#     if x%y==0:
#         break
# else:
#     n2.append(x)
# """
    # main()

    # code_p1 = 'ast_research/ch4_false/0.py'
    # code_snippet_1 = file_reader(code_p1)
    # code_ab = ast.parse(code_snippet)
    # code_ = py_parser.parse(bytes(code_, 'utf8')).root_node
    # visualize('ast_research/out/others/test_3', code_)
