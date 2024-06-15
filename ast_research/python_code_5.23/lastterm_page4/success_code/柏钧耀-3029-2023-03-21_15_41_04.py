# 输入学生姓名和成绩
names = input().split(',')
scores = eval(input())

# 组合姓名和成绩，形成嵌套列表
result = [[names[i], scores[i]] for i in range(len(names))]

# 输出结果
print(result)
