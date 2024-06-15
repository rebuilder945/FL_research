def  stuid(data2):
            a=[]
            for i in data2:
                    c=i[0:8]
                    a.append(c)
            return a

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

