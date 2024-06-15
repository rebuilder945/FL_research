names = input().split(',')  # 输入姓名，用逗号分隔
scores = list(map(int, input().split(',')))  # 输入成绩，用逗号分隔并转换成整数列表

# 将姓名和成绩配对成嵌套列表
pairs = [[name, score] for name, score in zip(names, scores)]

# 按照成绩升序排序
pairs.sort(key=lambda pair: pair[1])

# 输出嵌套列表
print(pairs)
