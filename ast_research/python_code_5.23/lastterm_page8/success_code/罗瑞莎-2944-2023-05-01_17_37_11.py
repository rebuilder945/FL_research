def  stuid(data2):
    lst = []
    a = ''
    for i in data2:
        a = i[:9]
        lst.append(a)
        a = ''
    return lst

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

