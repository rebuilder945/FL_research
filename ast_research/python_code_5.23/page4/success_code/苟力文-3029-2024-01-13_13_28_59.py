# 输入的姓名和成绩列表
names = input().split(",")
scores = list(map(int, input().split(",")))

# 创建一个新的列表来存储嵌套列表
nested_list = []

# 遍历姓名和成绩列表，将它们组合成嵌套列表并添加到新的列表中
for name, score in zip(names, scores):
    nested_list.append([name, score])

# 输出新的嵌套列表
print(nested_list)

