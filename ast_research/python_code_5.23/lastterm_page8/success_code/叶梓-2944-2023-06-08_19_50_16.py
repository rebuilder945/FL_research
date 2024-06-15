def  stuid(data2):
    data=[]
    for x in data2:
        data.append(x[0:8])
    return data

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

