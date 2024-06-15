def  stuid(data2):
    student_id = [x[:8] for x in data2]
    return student_id

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

