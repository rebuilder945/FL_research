n=eval(input())
x=2
y=1
c=0
while n>0:
    c+=x/y
    d=y
    y=x
    x=x+d
    n-=1
print("%.4f"%c)
