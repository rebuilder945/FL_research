n=eval(input())
a=1
b=2
c=0
c=c+b/a
f=a
a=2
d=b
b=3
for x in range (n-1):
    c=c+b/a
    g=a+f
    f=a
    a=g
    e=b+d
    d=b
    b=e
print("%.4f"%(c))
