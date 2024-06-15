def  stuid(data2):
    x=[]
    for i in data2:
        x.append(i[0,9])
    return x

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

