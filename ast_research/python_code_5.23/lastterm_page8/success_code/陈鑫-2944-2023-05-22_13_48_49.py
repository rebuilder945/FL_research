def  stuid(data2):
    b=[]
    for i in data2:
        b+=i[:8]
        b+=[ ]
    return b

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

