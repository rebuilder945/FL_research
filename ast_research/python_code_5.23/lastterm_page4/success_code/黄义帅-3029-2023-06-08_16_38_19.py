# 读取输入
names = input().split(',')
scores = eval(input())

# 组合成新的列表
result = [[name, score] for name, score in zip(names, scores)]

# 输出结果
print(result)


