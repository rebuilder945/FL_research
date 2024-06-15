def add_id(data2):
    student_id=[]
    for x in data2:
        student_id.append(x[0:8])
    return student_id    

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

