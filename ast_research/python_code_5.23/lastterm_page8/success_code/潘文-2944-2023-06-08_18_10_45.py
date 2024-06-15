def  stuid(data2):
    data2=list(data2)
    a=data2[:8]
    return a


data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

