def  stuid(data2):
    date3=[]
    for i in date2:
           date3.append(x[:8])
    return date3

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

