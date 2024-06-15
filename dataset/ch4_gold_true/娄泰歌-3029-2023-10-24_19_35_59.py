# 接收用户输入的姓名和成绩  
names = input().split(',')  
scores = input().replace('[', '').replace(']', '').split(',')  
  
# 使用列表解析来创建嵌套列表  
result = [[name, int(score)] for name, score in zip(names, scores)]  
  
# 输出结果  
print(result)
