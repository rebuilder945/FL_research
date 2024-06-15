def  stuid(data2):
        lst=[]
        for x in data2:
            number=x[0:8]
            lst.append(number)
        return lst

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

