n,m=input().split(" ")
n=int(n)
m=int(m)
x=[]
y=[]
if m<n or (m-n)<3 or m<0 or n<0 or n>=8:
    print("illegal input")
else:
    for i in range(n,m):
        x.append(i)
    for a in range(len(x)):
        for b in range(len(x)):
            for c in range(len(x)):
                if a!=b and b!=c and a!=c and x[a]!=0:
                    s=str(x[a])+str(x[b])+str(x[c])
                    if len(s)==3:
                        y.append(int(s))
    y.sort(reverse=False)
    for i in y:
        print(i,end=" ")

