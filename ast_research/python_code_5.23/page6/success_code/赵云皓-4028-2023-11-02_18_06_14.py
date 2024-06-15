a=eval(input())
c=[]
b=[]
if a>0 and isinstance(a,int)==True:
    for i in range(a+1):
        d=[]
        for x in range(2,i):
            d.append(i%x)
        if 0 in d:
            d=d
        else:
            c.append(i)
    for i in c:
        s=str(i)
        if i==1 or i==0:
            s=s
        elif s[0]==s[-1]:
            b.append(i)
        else:
            a=a
else:
    print("illegal input")
b=list(map(str,b))
print(" ".join(b))

