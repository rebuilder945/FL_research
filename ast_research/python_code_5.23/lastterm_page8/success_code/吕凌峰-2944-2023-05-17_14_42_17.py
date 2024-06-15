def  stuid(data2):
    d=[]
    for x in data2:
       d.append(x[0:9])
    return d

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

