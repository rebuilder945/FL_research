def  stuid(data2):
        a=[]
        for x in data2:
            b=x[0:8]
            b.append(a)
        return a     

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

