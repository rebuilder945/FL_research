def  stuid(data2):
    for m in data1:
        for n in i:
            if n.isdigital():
                continue
            else:
                remove(n)
    return data2

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

