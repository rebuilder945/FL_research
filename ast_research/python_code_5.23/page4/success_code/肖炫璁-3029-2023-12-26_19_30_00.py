# 从用户输入获取姓名和成绩
names_input = input()
scores_input = input()

# 将输入的字符串转换为列表
names = names_input.split(',')
scores = eval(scores_input)

# 组合姓名和成绩成嵌套列表
result = list(zip[names, scores])

# 输出结果
print(result)

