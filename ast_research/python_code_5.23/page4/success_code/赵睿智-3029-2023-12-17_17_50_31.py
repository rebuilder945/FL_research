# 输入姓名  
names = input().split(',')  
  
# 输入成绩  
scores = list(map(int, input().split(',')))  
  
# 确保两个列表长度相同  
if len(names) != len(scores):  
    print("输入的姓名和成绩数量不匹配")  
else:  
    # 组合姓名和成绩  
    result = [ [name, score] for name, score in zip(names, scores) ]  
      
    # 输出结果  
    print(result)
