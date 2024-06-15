def  stuid(data2):
    result=[]
    for d in data2:
    if ien(d)==8:
    result.append(d)
    return result

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

