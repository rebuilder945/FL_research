def  stuid(data2):
    ls=[]
    for x in data2:
        ls.append(x[:8])
    return ls

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

