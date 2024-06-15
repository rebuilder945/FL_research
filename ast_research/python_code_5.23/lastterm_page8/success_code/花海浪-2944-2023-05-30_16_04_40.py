def  stuid(data2):
    A=[]
    for x in data1:
           A.append(x[0:8])
    return A

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

