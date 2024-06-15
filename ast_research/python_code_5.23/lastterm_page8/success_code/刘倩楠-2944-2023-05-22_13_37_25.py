def  stuid(data2):
    ls=[]
    for x in data2:
        if x in range(10):
            ls.append(x)
        else:
            ls.append()
    return ls

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

