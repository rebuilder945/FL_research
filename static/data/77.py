student = eval(input())
info = student(1),student(3)#想要获取学生信息列表中的第一个和第三个元素，应该使用索引而不是函数调用
avg = sum(student[5]/len(student[5]))
print(info)
print("%.2f"%avg)