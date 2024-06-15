def  stuid(data2):
        n=len(data2)/10
        i=0
        ls=[]
        while True:
            if i<=n:
                m=data2[i:i+7]
                ls.append(m)
                i+=10
            else:
                 break
        return ls

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

