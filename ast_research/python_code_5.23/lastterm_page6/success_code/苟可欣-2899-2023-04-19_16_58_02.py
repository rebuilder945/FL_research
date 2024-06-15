k=input().split(" ")
n=int(k[0])
m=int(k[1])
if n+2>=m:
    print("illegal input")
else:
    lst=[]
    for x in range(n,m+1):
        lst.append(x)
        for i in lst:
            lst1=lst.copy()
            lst1.remove(i)
            for i1 in lst1:
                lst2=lst.copy()
                lst2.remove(i1)
                for i2 in lst2:
                    a=100*i+10*i1+i2
                    print(a,end=" ")
