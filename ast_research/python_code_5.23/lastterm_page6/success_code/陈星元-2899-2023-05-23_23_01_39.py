def com(n,m):
    ls=[]
    for x1 in range(n,m):
        for x2 in set(range(n,m))-{x1}:
            for x3 in set(range(n,m))-{x1,x2}:
                ls.append(str(x1)+str(x2)+str(x3))
    ls1=list(map(int,ls))
    ls2=ls1[:]
    for i in ls1:
        if i<=100:
            ls2.remove(i)
    ls2.sort()
    return ls2
ls=input().split(" ")
n=int(ls[0])
m=int(ls[1])
if n<m and 10>n>=0 and 10>m>=0:
    ls1=com(n,m)
    if len(ls1)!=0:
        for x in ls1:
            print(x,end=" ")
    else:
        print("illegal input")   
else:
    print("illegal input")


    
           


