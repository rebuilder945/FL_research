def  stuid(data2):
        for i in data2:
            a=[]
            for x in i:
            b=''
                a.append(str(x))
            for y in a[0:8]:
            b+=y
            i=int(b)
        return data2

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

