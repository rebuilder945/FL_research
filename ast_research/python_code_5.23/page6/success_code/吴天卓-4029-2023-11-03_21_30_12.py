n,x,m=input()
n,m=int(n),int(m)
s=""
if n>=0 and m-n>=3:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and b!=c and a!=c:
                    if a!=0:
                        s=s+(str(a)+str(b)+str(c))+" "+str(a)+str(c)+str(b)+" "
                    if b!=0:
                        s=s+str(b)+str(c)+str(a)+" "+str(b)+str(a)+str(c)+" "
                    if c!=0:
                        s=s+str(c)+str(a)+str(b)+" "+str(c)+str(b)+str(a)
    print(s)
else:
    print("illegal input")

