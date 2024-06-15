def  stuid(data2):
        lst=[]
        for i in data2:
              n=i[0:8:1]
              lst.append(n)
        return lst      

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

