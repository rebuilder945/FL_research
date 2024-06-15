def  stuid(data2):
        c=[]
        for x in data2:
              c.append(x[0:8])
        return c

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

