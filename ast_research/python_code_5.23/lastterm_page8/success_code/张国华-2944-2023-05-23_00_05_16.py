def  stuid(data2):
    result=[]
    for i in range(len(data2)):
                if len(data2[i])==10 and data2[i].isdigit():
                    result.append(data2[i])
    return result

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

