student = eval(input())
info = student[2:5]
avg = sum(int(x) for x in student[2:5])  
#将列表中的元素转换为整数
print(info)
print("%.2f" % avg)