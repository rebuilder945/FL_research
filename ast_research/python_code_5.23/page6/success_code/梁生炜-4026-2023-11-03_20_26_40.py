from re import A


n=eval(input())
x=2
y=1
m=0
while n>0:
    m=m+x/y
    a=y
    y=x
    x=x+a
    n-=1
print("%.4f"%m)
