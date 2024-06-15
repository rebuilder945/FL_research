def  stuid(data2):
           a=0
            b=len(data2[0])
            c=[]
            while a!=b:
                shuzi={'1','2','3','4','5','6','7','8','9','0'}
                if data2[0][a] in shuzi:
                    qie=data2[0][a:a+8]
                    c.append(qie)
                    a+=8
                else:
                    a+=1 
            return c

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

