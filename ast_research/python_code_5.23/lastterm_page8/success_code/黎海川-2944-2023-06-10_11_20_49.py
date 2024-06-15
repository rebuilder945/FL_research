def  stuid(data2):
    l=[]
    d=list(data2)
    for i in data2:
        l.append(i[0:8])
    return l

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

