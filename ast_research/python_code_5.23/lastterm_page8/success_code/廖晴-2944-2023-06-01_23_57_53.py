def  stuid(data2):
    s=[]
    for x in data2:
        s.append(x[:8])
    return s

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

