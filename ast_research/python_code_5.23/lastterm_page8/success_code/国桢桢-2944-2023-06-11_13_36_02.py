def  stuid(data2):
    id = []
    for i in ids:
     id.append(i[:8])
    return id

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

