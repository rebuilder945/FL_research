def  stuid(data2):
    a=[]
    for i in range(len(data2)):
      a.append(data2[i][0:7])
    return a

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

