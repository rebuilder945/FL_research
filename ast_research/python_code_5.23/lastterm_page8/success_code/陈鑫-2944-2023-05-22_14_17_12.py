def  stuid(data2):
    b=[]
    a=0
    for i in range(len(data2)):
        b[a]=data2[i][:8]
        a+=1
    return b

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

