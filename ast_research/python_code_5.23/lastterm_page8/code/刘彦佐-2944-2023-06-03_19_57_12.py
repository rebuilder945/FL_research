def  stuid(data2):
    
        m=[]
        for i in range(0,len(data2))):
            m.append(data2[i][0:7:])
        return m

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

