def  stuid(data2):
    lst=[]
    for i in range(len(data2)):
         lst.append(data2[i][:8])
    return lst

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

