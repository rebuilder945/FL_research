def  stuid(data2):
        data21=[]
        for i in data2:
            xuehao=i[:8]
            data21.append(xuehao)
        return data21

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

