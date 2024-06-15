
names = input().split(',') # 读入姓名列表
scores = input().split(',') # 读入成绩列表

# 去掉scores列表中的非数字元素
scores = [int(x) for x in scores if x.isdigit()]

# 将姓名和成绩组合成一个嵌套列表
lst = [[names[i], scores[i]] for i in range(len(scores))]

# 按照成绩升序排序
lst = sorted(lst, key=lambda x: x[1])

# 输出结果
print(lst)

