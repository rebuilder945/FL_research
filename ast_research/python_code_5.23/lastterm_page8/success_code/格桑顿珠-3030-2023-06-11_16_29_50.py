def create_nested_list(names, scores):
    nested_list = []

    for name, score in zip(names, scores):
        nested_list.append([name, int(score)])

    sorted_list = sorted(nested_list, key=lambda x: x[1])

    return sorted_list

# 输入学生姓名和成绩
name_input = "tom,james,jack"
score_input = "89,34,78"

# 将姓名和成绩转换为列表
names = name_input.split(",")
scores = score_input.split(",")

# 创建并排序嵌套列表
result = create_nested_list(names, scores)

# 输出结果
print(result)

