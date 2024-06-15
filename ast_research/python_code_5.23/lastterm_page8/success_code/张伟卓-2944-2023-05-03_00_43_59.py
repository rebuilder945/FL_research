def  stuid(data2):
        for i in data2:
            xue=i[:8]
            return xue

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

