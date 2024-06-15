def  stuid(data2):
      lst1=[]
      for I in data2:
         lst1.append(I[:8])
      return lst1

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

