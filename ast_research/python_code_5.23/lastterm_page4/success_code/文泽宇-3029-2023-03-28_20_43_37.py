# 读取输入
names = eval(input())
scores = eval(input())

# 将姓名和成绩组合成元组列表
result = []
for i in range(len(names)):
    result.append((names[i], scores[i]))

# 输出结果
print(result)
