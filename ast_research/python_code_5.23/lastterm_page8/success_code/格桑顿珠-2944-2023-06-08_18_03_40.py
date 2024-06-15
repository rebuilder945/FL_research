def  stuid(data2):
        num = []
        for i in data2:
            num.append(i[:8])
        return num

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

