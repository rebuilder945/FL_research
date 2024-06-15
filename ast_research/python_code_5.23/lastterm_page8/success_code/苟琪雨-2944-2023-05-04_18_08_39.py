def  stuid(data2):
    for m in data1:
        for n in m:
            if n.isdigit():
                continue
            else:
                remove(n)
    return data2

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

