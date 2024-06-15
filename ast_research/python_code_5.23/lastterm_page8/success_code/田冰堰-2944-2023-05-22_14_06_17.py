def  stuid(data2):
    for i in range(len(data2)):
        m=data2[i][:8]
    return m.split()

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

