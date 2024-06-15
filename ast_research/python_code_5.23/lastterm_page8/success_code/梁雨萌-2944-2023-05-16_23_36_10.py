def  stuid(data2):
        lis = []
        for i in data2:
            num =  i[0,8,1]
            lis.append(num)
        return lis

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

