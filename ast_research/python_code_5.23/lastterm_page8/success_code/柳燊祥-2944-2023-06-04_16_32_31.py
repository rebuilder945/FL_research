def  stuid(data2):
    for x in list(range(len(data2))):
        data2[x]=data2[x][0:8]
    return data2

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

