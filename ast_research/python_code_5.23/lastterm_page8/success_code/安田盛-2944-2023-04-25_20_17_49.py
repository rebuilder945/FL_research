def  stuid(data2):
    y=[int(i[0:8]) for i in data2]
    return y

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

