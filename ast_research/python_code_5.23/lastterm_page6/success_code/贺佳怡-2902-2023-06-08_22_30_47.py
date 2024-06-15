n=int(input())
s=0
x=0
m=2
b=1
while x<=n:
    s+=(m+x)/(b+x)
    m+=x
    b+=x
    x+=1
print("%.4f" % s)
