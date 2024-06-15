def  stuid(data2):
        result=[]
        for d in data2:
            x=d[0:7]
            result.append(x)
        return result

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

