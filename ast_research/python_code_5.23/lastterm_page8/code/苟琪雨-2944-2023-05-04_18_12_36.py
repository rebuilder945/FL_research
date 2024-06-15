def  stuid(data2):
    for m in data1:
    count==0
        for n in m:
            if n.isdigit():
                count+=1
            else:
                m=m[0:n-1]
                break
    return data2

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

