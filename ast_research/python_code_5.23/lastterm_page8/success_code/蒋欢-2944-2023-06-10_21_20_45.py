def  stuid(data2):
    ls=[]
    for x in data2:
        x2=x[:8]
        ls.append(x2)
    return ls

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

