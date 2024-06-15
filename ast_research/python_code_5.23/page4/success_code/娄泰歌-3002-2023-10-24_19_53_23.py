# 输入列表  
lst = list(map(int, input().split(',')))  
  
# 计算平均值  
avg = sum(lst) / len(lst)  
  
# 判断平均值类型，并输出结果  
if avg == int(avg):  
    print(int(avg))  
else:  
    print("{:.2f}".format(avg))
