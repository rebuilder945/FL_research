def  stuid(data2):
    ls1=[]
        for i in data1:
            a=i[0:8]
            ls1.append(a)
        return ls1


data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

