def  stuid(data2):
    b=[]
    a=0
    for i in data2:
        b[a]=i[0]
        print(b)
        a+=1
    return b

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

