def  stuid(data2):
    for i in data2.split():
        if type(i)==int:
            return i

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

