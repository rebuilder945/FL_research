def  stuid(data2):
    student_id = []  # 创建一个空列表，用于存储学号信息
    for i in range(0, len(data), 2):  # 循环遍历输入的数据，每次跳两个位置取出学号信息
          student_id.append(data[i])   # 将取出的学号添加到列表中return student_id

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

