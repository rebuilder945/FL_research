def  stuid(data2):
        a = []
        for i in data2:
            t = i[0:7]
            a.append(t)
        return a

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

