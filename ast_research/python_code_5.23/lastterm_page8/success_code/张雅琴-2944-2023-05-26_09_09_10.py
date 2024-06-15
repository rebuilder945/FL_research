def  stuid(data2):
    id=[]
    for i in data2:
        a=i[0,8]
        a=int(a)
        id.append(a)
    return id

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

