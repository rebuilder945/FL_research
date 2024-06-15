n=eval(input())
d=0
a=2
b=1
while n>0:
    n-=1
    e=b
    c=a/b
    d+=c
    b=a
    a=e+a
    
print("%.4f"%(d))
