def  stuid(data2):
        student_id = []
        for info in data2:
            if len(info) == 8:  # 学号长度为8位
                student_id.append(info)
        return student_id

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

