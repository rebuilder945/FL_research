# 获取输入，姓名和成绩分别用split()函数获取得到一个列表
names = input().strip().split(',')
scores = input().strip().split(',')

# 将成绩转换为整数
scores = [int(score) for score in scores]

# 使用zip()函数将姓名和成绩配对，并按照升序排序
result = sorted(list(zip(names, scores)), key=lambda x: x[1])

# 直接输出嵌套列表
print(result)

