def  stuid(data2):
    ls=[]
    for x in data2:
        m=x[0:7]
        ls.append(m)
    return ls

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

