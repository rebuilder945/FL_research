def  stuid(data2):
    ass=[]
    for x in data2:
        a=x[:8]
        ass.append(a)
    return ass

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

