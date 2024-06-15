def  stuid(data2):
    id=[]
    for i in data2:
        id.append(eval(i[0:8])
    return id

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

