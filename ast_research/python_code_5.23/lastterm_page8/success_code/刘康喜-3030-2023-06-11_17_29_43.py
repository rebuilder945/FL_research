names = input().split(',')  # 读入姓名列表
scores = input().split(',')  # 读入成绩列表

# 将成绩列表中的元素转换为整数类型
scores = [int(score) for score in scores]

# 将姓名和成绩配对形成嵌套列表
pairs = [[names[i], scores[i]] for i in range(len(names))]

# 按照成绩升序排序
pairs = sorted(pairs, key=lambda x: x[1])

# 直接输出嵌套列表
print(pairs)
