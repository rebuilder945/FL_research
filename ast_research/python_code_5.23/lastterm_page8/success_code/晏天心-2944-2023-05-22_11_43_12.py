def  stuid(data2):
    list1=[]
    for x in data2:
          a=x[0:8]
          list1.append(a)
    return list1

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

