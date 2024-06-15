def  stuid(data2):
    num=[]
    for x in data2:
        num.append(data2[:8])
    return num

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

