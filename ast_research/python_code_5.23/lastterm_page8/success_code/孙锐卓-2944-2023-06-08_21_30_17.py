def  stuid(data2):
    m=[]
    for x in data2:
        a=x[:8]
        m.append(a)
    return m      


data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

