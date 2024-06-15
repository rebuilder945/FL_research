n=eval(input())
a=1
b=1
c=0
s=2
x=1
sum=2
if n==1:
    print(2.0000)
else:
    while n-1:
        n-=1
        c=s
        s+=a
        a=c
        c=x
        x+=b
        b=c
        sum+=s/x
    print("%.4f"%(sum))
