n=int(input())
sums=0
x=2
y=1
while n>0:
    sums+x/y
    m=y
    y=x
    x=x+m
    n-=1
print("%.4f"%sums)
