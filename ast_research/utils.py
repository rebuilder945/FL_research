import ast
import pandas as pd
from sklearn.decomposition import PCA
import zss
import os
import math
import graphviz as gv
import subprocess
import numbers
import tree_sitter
import numpy as np
import matplotlib.pyplot as plt
from zss import simple_distance
from tree_sitter import Node
import re
import numpy as np
from uuid import uuid4 as uuid


class GraphRenderer:
    """
    this class is capable of rendering data structures consisting of
    dicts and lists as a graph using graphviz
    """

    graphattrs = {
        "labelloc": "t",
        "fontcolor": "white",
        "bgcolor": "#333333",
        "margin": "0",
    }

    nodeattrs = {
        "color": "white",
        "fontcolor": "white",
        "style": "filled",
        "fillcolor": "#006699",
    }

    edgeattrs = {
        "color": "white",
        "fontcolor": "white",
    }

    _graph = None
    _rendered_nodes = None

    @staticmethod
    def _escape_dot_label(str):
        return (
            str.replace("\\", "\\\\")
            .replace("|", "\\|")
            .replace("<", "\\<")
            .replace(">", "\\>")
        )

    def _render_node(self, node):
        if isinstance(node, (str, numbers.Number)) or node is None:
            node_id = uuid()
        else:
            node_id = id(node)
        node_id = str(node_id)

        if node_id not in self._rendered_nodes:
            self._rendered_nodes.add(node_id)
            if isinstance(node, dict):
                self._render_dict(node, node_id)
            elif isinstance(node, list):
                self._render_list(node, node_id)
            else:
                self._graph.node(node_id, label=self._escape_dot_label(str(node)))

        return node_id

    def _render_dict(self, node, node_id):
        self._graph.node(node_id, label=node.get("node_type", "[dict]"))
        for key, value in node.items():
            if key == "node_type":
                continue
            child_node_id = self._render_node(value)
            self._graph.edge(node_id, child_node_id, label=self._escape_dot_label(key))

    def _render_list(self, node, node_id):
        self._graph.node(node_id, label="[list]")
        for idx, value in enumerate(node):
            child_node_id = self._render_node(value)
            self._graph.edge(
                node_id, child_node_id, label=self._escape_dot_label(str(idx))
            )

    def render(self, data, out_dir: str, f_name: str, *, label=None):
        # create the graph
        graphattrs = self.graphattrs.copy()
        if label is not None:
            graphattrs["label"] = self._escape_dot_label(label)
        graph = gv.Digraph(
            graph_attr=graphattrs, node_attr=self.nodeattrs, edge_attr=self.edgeattrs
        )

        # recursively draw all the nodes and edges
        self._graph = graph
        self._rendered_nodes = set()
        self._render_node(data)
        self._graph = None
        self._rendered_nodes = None

        # display the graph
        graph.render(
            directory=out_dir,
            filename=f_name,
            format="png",
            view=False,
            # outfile=os.path.join(out_dir, f_name)
        )


class SubTreeNode:
    def __init__(self, ts_node: Node, code_id: int):
        self.ts_node = ts_node
        self.subtree_id = 0
        self.code_id = code_id
        self.type = 0
        self.tf_idf = 0

    def __eq__(self, value: object, cent_encoder, threshold: int = 3) -> bool:
        if isinstance(value, SubTreeNode):
            # edit dis
            # dis = simple_distance(
            #     get_tree4distance(self.ts_node), get_tree4distance(value.ts_node)
            # )

            # cent encoding
            dis = np.linalg.norm(
                np.array(cent_encoder.sing_tree_encode(self))
                - np.array(cent_encoder.sing_tree_encode(value))
            )

            # print(dis)

            if dis < threshold:
                return True
            else:
                return False

        return False

    def __hash__(self) -> int:
        return hash(self.subtree_id)

    def __str__(self) -> str:
        return travers_dfs(self.ts_node)


def transform_ast4treesitter(code_ast: SubTreeNode):
    """
    params:
    :code_ast: the ast to transform
    """
    # tree-sitter
    node = {
        to_camelcase(f"{index}"): transform_ast4treesitter(k)
        for index, k in enumerate(code_ast.children)
    }
    node["node_type"] = to_camelcase(code_ast.type)
    return node


def get_tree4distance(root):
    return zss.Node(
        label=to_camelcase(root.type),
        children=[get_tree4distance(k) for k in root.children],
    )


def height_of_tree(root):
    # 如果树为空，则高度为0
    if not root:
        return 0

    # 如果节点没有子节点，则高度为1
    if not root.children:
        return 1

    # 递归计算每个子节点的高度，取最大值并加1（加1是因为要包括当前节点）
    max_child_height = 0
    for child in root.children:
        child_height = height_of_tree(child)
        max_child_height = max(max_child_height, child_height)

    return max_child_height + 1


def get_all_subtrees(root: Node, depth_range: tuple, code_id: int) -> list[SubTreeNode]:
    """
    获取一棵树的所有子树，并编号来自哪个代码
    : param root: 树的根节点
    : param depth_range: 子树的深度范围，例如(0, 10)表示深度在0到10之间的子树
    : param code_id: 代码的编号
    """
    subtrees = []

    # 递归函数，遍历树并收集所有子树
    def traverse(node):
        if depth_range[1] > height_of_tree(node) >= depth_range[0] and not (
            node.type == "block" or node.type == "expression_statement"
        ):
            # TODO: block未真正有效去除
            # 将当前节点及其子节点作为一个子树添加到列表中
            subtrees.append(SubTreeNode(node, code_id))
            # subtrees.append([get_custom_subtree(node)])

        # print(node.text)
        for child in node.children:
            traverse(child)

    # 从根节点开始递归遍历
    traverse(root)

    return subtrees

def get_custom_subtree(root: Node):
    """
        自定义保留从treesitter树中的所需节点
    """
    return {
        "type": to_camelcase(root.type),
        "children": [
            get_custom_subtree(child)
            if child.type != "block" and child.type != "expression_statement"
            else get_custom_subtree(child.children[0])
            for child in root.children
        ],
    }


def travers_dfs(root):
    if root == None:
        return ""
    path = root.type
    for child in root.children:
        path += " " + travers_dfs(child)
    return path


def visualize(report_path, root_node):
    """
        可视化任意树结构
        : param report_path: 输出路径，仅为输出文件名，不包含后缀；
        : param root_node: 树的根节点
    """
    renderer = GraphRenderer()
    out_dir = os.path.dirname(report_path)
    f_name = os.path.basename(report_path)
    # if isinstance(root_node, ast.AST):
    #     transformed_ast = transform_ast(root_node)
    #     renderer.render(
    #         transformed_ast, out_dir=out_dir, f_name=f_name
    #     )
    # else:
    transformed_ast = transform_ast4treesitter(root_node)
    renderer.render(transformed_ast, out_dir=out_dir, f_name=f_name)


def histogram_draw(data: list, type_num: int, output_path: str):
    """
    绘制直方图
    : param data: [elements...], 每个element即可，会进行计数;
    : param type_num: set(element)长度；
    : param output_path: 输出路径，仅为输出文件所在文件夹；
    """
    # 绘制直方图统计y_pred的分布
    plt.clf()
    plt.figure(figsize=(10, 5))
    plt.hist(data, bins=np.arange(0, type_num + 1) - 0.5, rwidth=0.8)
    hist, _ = np.histogram(data, bins=np.arange(0, type_num + 1) - 0.5)
    # 在每个bar上方显示数量
    for x, y in zip(range(len(hist)), hist):
        plt.text(x, y, str(y), ha="center", va="bottom")
    plt.title("Histogram of y_pred")
    plt.xlabel("Cluster")
    plt.ylabel("Frequency")
    plt.savefig(os.path.join(output_path, "histogram.png"))


def draw_cluster(
    dataset: pd.DataFrame,
    centers: np.ndarray,
    sample_dim: int,
    cluster_num: int,
    labels: list,
    output_path: str,
):
    """
    绘制聚类后的散点图
    """
    center_array = np.array(centers)
    if sample_dim > 2:
        dataset = PCA(n_components=2).fit_transform(dataset)  # 如果属性数量大于2，降维
        center_array = PCA(n_components=2).fit_transform(
            center_array
        )  # 如果属性数量大于2，降维
    else:
        dataset = np.array(dataset)
    # 做散点图
    label = np.array(labels)
    plt.clf()
    # sizes = list(range(4, 10))
    plt.scatter(dataset[:, 0], dataset[:, 1], marker="o", c="black", s=4)  # 原图
    from ast_research.const import colors

    # 循换打印k个簇，每个簇使用不同的颜色
    for i in range(cluster_num):
        plt.scatter(
            dataset[np.nonzero(label == i), 0][0],
            dataset[np.nonzero(label == i), 1][0],
            c=colors[i],
            s=15,
            marker="o",
        )
    plt.scatter(
        center_array[:, 0], center_array[:, 1], marker="x", color="m", s=30
    )  # 聚类中心
    # plt.show()
    plt.savefig(os.path.join(output_path, "cluster.png"))


def cal_tfidf(cls_dict: dict, sub_trees: list, code_num):
    for cls in cls_dict:
        # tf_cls = 单个词频 / 所有词总频次 = 单个类的子树数量 / 所有子树数量
        cls_tf = len(cls_dict[cls]) / len(sub_trees)
        # idf_cls = log(文档数量 / 单个词出现在的文档数量) = log(代码数量 / 单个类所有子树所在代码数量)
        cls_idf = math.log(
            code_num / len(set([subtree.code_id for subtree in cls_dict[cls]]))
        )
        for subtree in cls_dict[cls]:
            subtree.tfidf = cls_tf * cls_idf


def to_camelcase(string):
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", string).lower()


def file_reader(file_path: str):
    with open(file_path, "r", encoding="utf8") as f:
        code = f.read()
    return code


def file_writer(file_path: str, content: str):
    with open(file_path, "w", encoding="utf8") as f:
        f.write(content)


def folder_check(path):
    """
        检查路径是否存在，不存在则递归地创建沿途所有文件夹
    """
    path_ = path.split("/")
    if len(path_) == 0:
        raise ValueError("path is empty")
    if len(path_) == 1:
        if not os.path.exists(path):
                os.mkdir(path)
        return
    last = path_[0]
    if not os.path.exists(last):
                os.mkdir(last)
    for index in range(1, len(path_)):
        tmp_path = os.path.join(last, path_[index])
        if not os.path.exists(tmp_path):
                os.mkdir(tmp_path)
        last = tmp_path


if __name__ == "__main__":
    pass
    # folder_check("ast_research/out/match22_ouput/False_5_20-1/3/2/100/23/1/2/4/31/2")

    # class cusNode:
    #     def __init__(self, type, children=[]):
    #         self.type = type
    #         self.children = children

    # tree = cusNode(
    #     "1", [cusNode("2", [cusNode("3")]), cusNode("4", [cusNode("1"), cusNode("10")])]
    # )
    # visualize('ast_research/out/others/test', tree)
