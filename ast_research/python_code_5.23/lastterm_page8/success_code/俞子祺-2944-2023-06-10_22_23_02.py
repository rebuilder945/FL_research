def  stuid(data2):
    a=0
    ls=[]
    for i in data2:
        m=i[0:8]
        ls.append(m)
    return ls

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

