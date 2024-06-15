def  stuid(data2):
        stu={}
        data2=input().split()
        lst=[]
        lst2=[]
        for x,y in stu.items():
            lst.append(int(x))
            lst2.append(y)
        return lst

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

