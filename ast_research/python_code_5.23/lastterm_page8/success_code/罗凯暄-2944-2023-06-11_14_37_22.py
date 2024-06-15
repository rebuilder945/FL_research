def  stuid(data2):
        student_id = []
        for i in range(0, len(data), 2):
            if len(data[i]) == 8:
                student_id.append(data[i])
        return student_id


data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

