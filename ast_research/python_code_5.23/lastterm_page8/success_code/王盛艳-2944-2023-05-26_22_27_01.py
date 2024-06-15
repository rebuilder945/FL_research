def  stuid(data2):
    student_id = []
    for i in range(len(data1)):
        if len(data1[i]) == 8 and data1[i].isdigit():
            student_id.append(data1[i])
            return student_id

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

