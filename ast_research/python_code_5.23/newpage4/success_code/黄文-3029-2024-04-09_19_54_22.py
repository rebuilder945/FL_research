# 获取输入并使用eval将其转换为列表
names = input().split(',')
scores = eval(input())

# 使用zip函数将两个列表组合起来
combined = zip(names, scores)

# 使用列表推导式将迭代器转换为一个嵌套列表
result_list = [list(pair) for pair in combined]

# 输出形成的新列表
print(result_list)


