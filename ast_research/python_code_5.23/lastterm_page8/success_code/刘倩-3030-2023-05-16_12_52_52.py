# 输入姓名和成绩
names = input().split(',')
scores = list(map(int, input().split(',')))

# 将姓名和成绩配对，并转化为列表
pairs = list(zip(names, scores))

# 根据成绩排序，并打印结果
result = sorted(pairs, key=lambda x: x[1])

# 将元组转化为列表
result = [list(pair) for pair in result]

print(result)

