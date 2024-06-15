def  stuid(data2):
    m=[]
    for x in data2:
        m.append(x[0:8:1])
    return m

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

