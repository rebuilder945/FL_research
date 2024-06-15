def  stuid(data2):
        ab=[]
        for i in data2:
            ab.append(i[:8])
        return ab

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

