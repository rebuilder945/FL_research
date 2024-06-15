def  stuid(data2):
    student_id = []
    for data in data2:
        student_id.append(data[0:8])
    return student_id

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

