def  stuid(data2):
    data1=[]
    for x in data2:
        data1.append(x[0:8])
    return data1

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

