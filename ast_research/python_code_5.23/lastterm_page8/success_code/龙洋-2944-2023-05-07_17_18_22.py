def  stuid(data2):
    y=[]
    for x in data2:
      y.append(x[0:8])
    return y

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

