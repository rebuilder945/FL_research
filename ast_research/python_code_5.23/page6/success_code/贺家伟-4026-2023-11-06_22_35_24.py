a=2
b=1
d=a/b
s=2
c=eval(input())
for i in range(0,c-1):
    e=b
    b=a
    a=a+e
    d=a/b
    s+=d
print("%.4f"%(s))
