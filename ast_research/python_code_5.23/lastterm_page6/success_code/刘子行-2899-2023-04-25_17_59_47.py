n,m=input().split(" ")
n=int(n)
m=int(m)
k=0
if m-n<3 or m<=0 or n>=7:
    k=1
b=[x for x in range(n,m)]
c=[]
h1=set(b)
for x in range(100,m*10**2):
    a=map(int,[i for i in str(x)])
    a=sorted(a)
    h0=set(a)
    if h0.issubset(h1) and len(h0)==3:
        c.append(x)
if k==1:
    print('illegal input')
else:
    for x in range(len(c)):
        print("%d "%c[x],end="")

