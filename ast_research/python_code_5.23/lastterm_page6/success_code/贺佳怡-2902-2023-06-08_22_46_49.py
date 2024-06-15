n=int(input())
s=0
x=0
m=2
b=1
c=1
while x<=n:
    s+=m/b
    m+=b
    b=m-c
    c=m
    x+=1
print("%.4f" % s)
