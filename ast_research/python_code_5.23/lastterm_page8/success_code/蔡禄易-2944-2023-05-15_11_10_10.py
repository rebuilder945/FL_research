def  stuid(data2):
    n = [ ]
    for i in data2:
        s = i [0:4]
        n.append(s)
    return n

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

