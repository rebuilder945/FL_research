def  stuid(data2):
    v=[]
    for i in data2:
        v.append(i[:8])
    return v

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

