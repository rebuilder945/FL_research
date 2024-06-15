def  stuid(data2):
    for i in data2:
        for x in i :
            del x[-1]
            del x[-2]
    return data2

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

