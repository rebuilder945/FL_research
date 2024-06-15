names = input().split(',')  # 输入姓名列表  
scores = input().split(',')  # 输入成绩列表  
  
# 将字符串类型的成绩转换为浮点数类型  
for i in range(len(scores)):  
    scores[i] = int(scores[i])  
  
# 创建嵌套列表，将姓名和成绩配对  
nested_list = [[name, score] for name, score in zip(names, scores)]  
  
# 按照成绩升序排序并输出  
nested_list.sort(key=lambda x: x[1])  
print(nested_list)
