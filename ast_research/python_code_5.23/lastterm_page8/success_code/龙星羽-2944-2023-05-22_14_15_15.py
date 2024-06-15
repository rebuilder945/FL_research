def  stuid(data2):
    ls=[]
    for x in data2:
        ls1=list(x)[0:8]
        s=''
        for i in ls1:
            s=s+i
        ls.append(s)
    return ls

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

