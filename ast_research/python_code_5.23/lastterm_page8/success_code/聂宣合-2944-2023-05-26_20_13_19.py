def  stuid(data2):
        lst=[]
        for r in data2:
            lst.append(r[:8])
        return lst

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

