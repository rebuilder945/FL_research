x=2
y=1
sums=0
n=eval(input())
while n>0:
    sums=sums+x/y
    m=y
    y=x
    x=x+m
    n-=1
print("%4f"%sums)

