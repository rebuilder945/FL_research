def  stuid(data2):
            sd=[]
            for i in data2:
                    i2=str(i)[:8]
                    sd.append(i2)
            return sd

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

