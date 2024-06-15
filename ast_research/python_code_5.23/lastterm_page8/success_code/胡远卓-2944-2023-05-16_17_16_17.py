def  stuid(data2):
    tmp=[]
    for x in data2:
        tmp.append(x[:8])
    return tmp

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

