def  stuid(data2):
    list=[]
    for i in data2:
        list.append(i[0:7])
    return list

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

