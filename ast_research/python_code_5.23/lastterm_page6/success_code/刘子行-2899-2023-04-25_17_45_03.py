n,m=input().split(" ")
n=int(n)
m=int(m)
k=0
if m-n<3 or m<=0 or m-n>3:
    k=1
b=[x for x in range(n,m)]
c=[]
for x in range(100,m*10**2):
    a=map(int,[i for i in str(x)])
    a=sorted(a)
    if a==b:
        c.append(x)
if k==1:
    print('illegal input')
else:
    for x in range(len(c)):
        print("%d "%c[x],end="")

