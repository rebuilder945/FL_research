def  stuid(data2):
    list=[]
    for i in data2:
        ni=i[:8]
        list.append(ni)

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

