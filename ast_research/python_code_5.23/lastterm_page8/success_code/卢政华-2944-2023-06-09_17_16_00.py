def  stuid(data2):
    result=[]
    for i in data2:
            result.append(i[:8])
    return result

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

