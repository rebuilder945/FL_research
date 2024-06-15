def  stuid(data2):
    for i in data2:
        del i[-1]
        del i[-2]
    return data2

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

