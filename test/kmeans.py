class Kmeans:
    def __init__(self, k, max_iterations=100):
        self.k = k
        self.max_iterations = max_iterations
        self.centroids = None
        self.clusters = None

    def initialize_centroids(self, data, k):
        # 从数据集中随机选择k个点作为初始质心
        centers = data[np.random.choice(data.shape[0], k, replace=False)]
        return centers


    def get_clusters(self, data, centroids):
        # 计算数据点与质心之间的距离，并将数据点分配给最近的质心
        distances = np.linalg.norm(data[:, np.newaxis] - centroids, axis=2)
        cluster_labels = np.argmin(distances, axis=1)
        return cluster_labels


    def update_centroids(self, data, cluster_labels, k):
        # 计算每个簇的新质心，即簇内数据点的均值
        new_centroids = np.array([data[cluster_labels == i].mean(axis=0) for i in range(k)])
        return new_centroids


    def k_means(self, data, k, T, epsilon):
        start = time.time()  # 开始时间，计时
        # 初始化质心
        centroids = self.initialize_centroids(data, k)
        t = 0
        while t <= T:
            # 分配簇
            cluster_labels = self.get_clusters(data, centroids)

            # 更新质心
            new_centroids = self.update_centroids(data, cluster_labels, k)

            # 检查收敛条件
            if np.linalg.norm(new_centroids - centroids) < epsilon:
                break
            centroids = new_centroids
            print("第", t, "次迭代")
            t += 1
        print("用时：{0}".format(time.time() - start))
        return cluster_labels, centroids


    # 计算聚类指标
    def clustering_indicators(self, labels_true, labels_pred):
        if type(labels_true[0]) != int:
            labels_true = LabelEncoder().fit_transform(df[columns[len(columns) - 1]])  # 如果数据集的标签为文本类型，把文本标签转换为数字标签
        f_measure = f1_score(labels_true, labels_pred, average='macro')  # F值
        accuracy = accuracy_score(labels_true, labels_pred)  # ACC
        normalized_mutual_information = normalized_mutual_info_score(labels_true, labels_pred)  # NMI
        rand_index = rand_score(labels_true, labels_pred)  # RI
        ARI = adjusted_rand_score(labels_true, labels_pred)
        return f_measure, accuracy, normalized_mutual_information, rand_index, ARI


    # 绘制聚类结果散点图
    def draw_cluster(self, dataset, centers, labels):
        center_array = array(centers)
        if attributes > 2:
            dataset = PCA(n_components=2).fit_transform(dataset)  # 如果属性数量大于2，降维
            center_array = PCA(n_components=2).fit_transform(center_array)  # 如果属性数量大于2，降维
        else:
            dataset = array(dataset)
        # 做散点图
        label = array(labels)
        plt.scatter(dataset[:, 0], dataset[:, 1], marker='o', c='black', s=7)  # 原图
        # plt.show()
        colors = np.array(
            ["#FF0000", "#0000FF", "#00FF00", "#FFFF00", "#00FFFF", "#FF00FF", "#800000", "#008000", "#000080", "#808000",
            "#800080", "#008080", "#444444", "#FFD700", "#008080"])
        # 循换打印k个簇，每个簇使用不同的颜色
        for i in range(k):
            plt.scatter(dataset[nonzero(label == i), 0], dataset[nonzero(label == i), 1], c=colors[i], s=7, marker='o')
        # plt.scatter(center_array[:, 0], center_array[:, 1], marker='x', color='m', s=30)  # 聚类中心
        plt.show()