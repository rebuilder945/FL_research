n=eval(input())
a=1
b=2
c=0
while n>0:
    c=c+b/a
    d=b
    b=b+a
    a=d
    n-=1
print("%.4f"%c)
    




