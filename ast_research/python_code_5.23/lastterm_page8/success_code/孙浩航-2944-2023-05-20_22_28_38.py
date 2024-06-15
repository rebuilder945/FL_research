def  stuid(data2):
            xx=[]
            aa=[]
            for x in data2:
                    xx.append(x)
            for i in xx:
                ww=i[0:8]
                aa.append(ww)
            return aa

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

