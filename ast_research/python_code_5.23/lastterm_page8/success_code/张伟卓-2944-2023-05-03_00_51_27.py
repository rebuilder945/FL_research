def  stuid(data2):
        ls=[]
            
        for i in data2:
            xue=i[:8]
            ls.append(xue)
        return ls

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

