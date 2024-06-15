def  stuid(data2):
        ls = []
        for x in data2:
            ls.append(x[0]+x[1]+x[2]+x[3]+x[4]+x[5]+x[6]+x[7])
        return ls

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

