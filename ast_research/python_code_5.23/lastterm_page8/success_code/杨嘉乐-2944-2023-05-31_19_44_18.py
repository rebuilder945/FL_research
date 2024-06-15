def  stuid(data2):
    for i in data2:
        nm=""
        for x in i:
            if x.isdigit():
                nm+=x
        i=nm
    return data2

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

