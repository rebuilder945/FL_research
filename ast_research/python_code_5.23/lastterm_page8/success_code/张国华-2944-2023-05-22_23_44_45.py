def  stuid(data2):
    student_id = []
    for i in range(len(data2)):
       if len(data2[i]) == 8:
            student_id.append(data2[i])
    return student_id

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

