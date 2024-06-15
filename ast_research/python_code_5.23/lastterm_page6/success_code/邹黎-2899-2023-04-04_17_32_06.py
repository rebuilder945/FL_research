n,m=map(int,input().split())
lst1=[]
if m-n<3 or  m<0 or n<0 or m>10:
    print("illegal input")
else:
    lst0=[x for x in range(n,m,1)]
    for a in lst0:
        for b in lst0:
            for c in lst0:
                if a!=b and b!=c and a!=0 and a!=c :
                    d=100*a+10*b+c
                    print(d,end=" ")
                    


