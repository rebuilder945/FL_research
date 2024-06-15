n,m=input().split(' ')
n=int(n)
m=int(m)
a=[]
b=[]
if n>m or (m-n)<3 or n<0 or m<0 or n>8:
    print("illegal input")
else:
    for x in range(n,m):
        a.append(x)
    for x in range(len(a)):
        for y in range(len(a)):
            for z in range(len(a)):
                if x!=y and x!=z and y!=z and a[x]!=0:
                    c=str(a[x])+str(a[y])+str(a[z])
                    if c not in b:
                        b.append(c)
                    else:
                        pass
                else:
                    pass
    for y in b:
        y=int(y)
        print("%d "%y,end="")
