def  stuid(data2):
        list1=[]
        for i in data2:
            list1=list1+[i[0:8]]
        return list1    

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

