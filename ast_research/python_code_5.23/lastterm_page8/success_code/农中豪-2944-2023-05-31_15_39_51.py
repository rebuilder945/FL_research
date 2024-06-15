def  stuid(data2):
    s2 = [temp[:8] for temp in data2.split(' ')]
    return s2

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

