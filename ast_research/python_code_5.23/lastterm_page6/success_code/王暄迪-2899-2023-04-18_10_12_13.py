n,m=input().split()
n=int(n)
m=int(m)
sums=[]
sums1=[]
if n<0 or m<0 or m-n<3 or n>8:
    print("illegal input")
else:
    for i in range(n,m):
        sums.append(i)
    for x in range(len(sums)):
        for y in range(len(sums)):
            for z in range(len(sums)):
                if x!=y and x!=z and y!=z and sums[x]!=0:
                    s1=str(sums[x])+str(sums[y])+str(sums[z])
                    if s1 not in sums1:
                        sums1.append(s1)
                    else:
                        pass
                else:
                    pass
    for q in sums1:
        q=int(q)
        print("%d "%q,end="")
