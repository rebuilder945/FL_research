def  stuid(data2):
    li = []
    for i in data2:
        li.append(i[:8])
    return li

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

