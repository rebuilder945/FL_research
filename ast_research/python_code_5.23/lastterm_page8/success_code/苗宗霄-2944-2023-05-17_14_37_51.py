def  stuid(data2):
        student_id = []  
        for i in range(0, len(data), 2): 
            id = data[i]
            if len(id) == 8:   # 需要判断提取出来的是否为8位学号
                student_id.append(id)   
        return student_id

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

