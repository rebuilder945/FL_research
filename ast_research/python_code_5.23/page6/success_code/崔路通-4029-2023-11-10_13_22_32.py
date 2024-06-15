n,m=input().split()
n,m=int(n),int(m)
if type(n)==int and type(m)==int and 0<n<m<10:
    lst1=[str(x) for x in range(n,m)]
    lst=lst1.copy()
    ls=lst.copy()
    lst2=[]
    for a in lst1:
        for b in lst:
            for c in ls:
                if a!=b and b!=c and a!=c:
                    lst2.append(a+b+c)

    
else :
    print("illegal input")


