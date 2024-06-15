def  stuid(data2):
    l=[]
    for x in date2:
        l.append(x[0:8])
    return l
        

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

