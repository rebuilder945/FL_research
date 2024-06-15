def sort_scores(names, scores):
    # 将姓名和成绩配对起来，形成嵌套列表
    nested_list = [[name, int(score)] for name, score in zip(names, scores)]
    # 按照成绩升序排序
    sorted_list = sorted(nested_list, key=lambda x: x[1])
    return sorted_list

# 获取学生姓名和成绩
names = input().split(",")
scores = input().split(",")
# 调用函数进行排序
result = sort_scores(names, scores)
# 输出结果
print(result)
