def  stuid(data2):
    s=[]
    for i in data2:
        s.append(i[:8])

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

