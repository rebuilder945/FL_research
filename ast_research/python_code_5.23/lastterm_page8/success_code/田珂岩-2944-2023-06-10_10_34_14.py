def  stuid(data2):
    ids = []
    for x in data2:
        ids.append(x)
    return ids
        

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

