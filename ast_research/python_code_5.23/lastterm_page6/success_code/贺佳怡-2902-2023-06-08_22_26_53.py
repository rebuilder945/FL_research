n=int(input())
s=0
x=1
while x<=n:
    s+=(x+1)/x
    x+=1
print("%.4f" % s)
