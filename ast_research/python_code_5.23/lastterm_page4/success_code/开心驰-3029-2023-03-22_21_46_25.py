# 从标准输入中读取学生姓名和考试成绩
names = input().split(',')  # 以逗号分隔姓名
scores = eval(input())  # 使用eval函数将输入的字符串转换为列表

# 将学生姓名和考试成绩组合成嵌套列表
result = [[name, score] for name, score in zip(names, scores)]

# 输出组合后的新列表
print(result)

