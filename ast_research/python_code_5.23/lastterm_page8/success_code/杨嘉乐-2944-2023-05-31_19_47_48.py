def  stuid(data2):
    new=[]
    for i in data2:
        l=list(i)
        del l[-1]
        new.append(str(l))
    return new

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

