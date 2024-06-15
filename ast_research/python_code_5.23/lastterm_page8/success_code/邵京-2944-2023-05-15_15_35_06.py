def  stuid(data2):
    id=[]
    for x in data2:
        id.append(x[0:8])
    return id

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

