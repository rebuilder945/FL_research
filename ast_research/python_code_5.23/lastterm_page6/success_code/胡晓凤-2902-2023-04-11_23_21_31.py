a=eval(input())
x=2
y=1
sums=0
while a>0:
    sums=sums+x/y
    m=y
    y=x
    x=x+m
    a-=1
print("%.4f"%sums)

