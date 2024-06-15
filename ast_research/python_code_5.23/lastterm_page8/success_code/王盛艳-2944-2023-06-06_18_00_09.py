def  stuid(data2):
    ls1 = []
    for i in data2:
        ls1.append(i[:8])
    return ls1

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

