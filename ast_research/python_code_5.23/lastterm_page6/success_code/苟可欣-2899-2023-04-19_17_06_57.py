k=input().split(" ")
n=int(k[0])
m=int(k[1])
if n+2>=m or n<0 or m <0 or n>=10 or m>=10:
    print("illegal input")
else:
    lst=[]
    for x in range(n,m):
        lst.append(x)
    for i in lst:
        lst1=lst.copy()
        lst1.remove(i)
        for i1 in lst1:
            lst2=lst1.copy()
            lst2.remove(i1)
            for i2 in lst2:
                a=100*i+10*i1+i2
                if a>100:
                    print(a,end=" ")
