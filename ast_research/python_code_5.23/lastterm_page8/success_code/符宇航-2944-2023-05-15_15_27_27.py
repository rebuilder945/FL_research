def  stuid(data2):
            data3=[]
            for i in data2:
                    i1 = i[0:8]
                    data3.append(i1)
            return data3

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

