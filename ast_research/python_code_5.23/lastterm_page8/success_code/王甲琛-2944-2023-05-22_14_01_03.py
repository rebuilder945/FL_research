def  stuid(data2):
    
        lst=[]
        lst2=[]
        for x in data2:
            lst.append(x)
        for a in lst:
            i=a[0,8]
            lst2.append(i)
        return(lst2)      

data1=input().split()
student_id=stuid(data1)
for x in student_id:
    print(x,end=" ")


        

