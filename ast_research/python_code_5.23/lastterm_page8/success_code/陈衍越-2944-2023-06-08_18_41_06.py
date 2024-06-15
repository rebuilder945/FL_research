def  stuid(data2):
    xh=[]
    for i in data2:
         xh.append(i[:8])
    return xh

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

