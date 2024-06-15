def  stuid(data2):
    new = []
    for x in data2:
        new.append(x[:8])
    return new

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

