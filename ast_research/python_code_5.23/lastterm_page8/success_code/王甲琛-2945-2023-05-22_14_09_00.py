def add_id(data2):
        lst=[]
        lst2=[]
        for x in data2:
            lst.append(x)
        for a in lst:
            b=float(a)
            i=b[0,8]
            lst2.append(i)
        return(lst2)  

data1=input().split()
result=add_id(data1)
for x in result:
    print(x,end=" ")

