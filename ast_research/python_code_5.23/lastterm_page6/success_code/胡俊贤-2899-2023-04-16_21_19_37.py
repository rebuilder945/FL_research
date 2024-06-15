ls=input().split()
n,m=map(int,ls)
if m-n>=3 and  n>=0 and m<=10:
    for a in range(n,m):
        for b in range(n,m):
            for c in  range(n,m):
                if a!=b and b!=c and c!=a:
                    s=a*100+b*10+c
                    if a!=0:
                        print(s,end=" ")
else:
    print('illgal input')            
                    
