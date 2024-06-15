def  stuid(data2):
                m=[]
                for i in data2:
                    m.append(i[:8])
                return m

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

