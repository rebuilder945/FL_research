def  stuid(data2):
    lst = []
    for x in data2:
          if len(x) == 2:
               lst.append(x)
    return lst

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

