x=2
y=1
n=int(input())
sums=0
while n>0:
    sums=sums+x/y
    m=y
    y=x
    x=x+m
    n-=1
print("%.4f"%sums)

