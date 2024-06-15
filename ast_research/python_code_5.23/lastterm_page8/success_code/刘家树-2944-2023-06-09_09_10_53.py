def  stuid(data2):
    l=[]
    for x in data2:
        l.append(x[:7:])

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

