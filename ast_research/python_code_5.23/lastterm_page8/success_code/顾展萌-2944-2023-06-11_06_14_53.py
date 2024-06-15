def  stuid(data2):
    ids = []
    for data in data2:
          if len(data) == 8:
             ids.append(data)
    return ids

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

