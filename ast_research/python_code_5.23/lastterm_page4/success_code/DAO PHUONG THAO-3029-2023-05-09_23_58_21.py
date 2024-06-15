name = input().split(',') # 输入姓名，以逗号分隔，转换为列表
scores = eval(input()) # 输入成绩，以列表的形式输入

result = [] # 定义一个空列表用于存储结果

for i in range(len(names)):
    result.append([name[i], scores[i]]) # 将每个姓名和对应的成绩组合成一个子列表，
    
print(result) # 输出结果
