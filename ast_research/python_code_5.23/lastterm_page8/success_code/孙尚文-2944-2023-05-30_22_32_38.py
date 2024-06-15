def  stuid(data2):
            d=[]
            for i in data2:
                    c=i[:8]
                    d.append(c)
            return d

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

