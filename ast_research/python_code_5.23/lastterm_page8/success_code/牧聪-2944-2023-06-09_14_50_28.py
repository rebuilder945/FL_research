def  stuid(data2):
    date3=[]
    for x in date2:
        t=x[0:8]
        date3.append(t)
    return date3

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

