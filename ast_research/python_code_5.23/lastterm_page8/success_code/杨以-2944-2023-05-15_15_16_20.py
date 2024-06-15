def  stuid(data2):
    ls=[]
    for x in data2:
      s=x[0:8]
      ls.append(s)
    return ls

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

