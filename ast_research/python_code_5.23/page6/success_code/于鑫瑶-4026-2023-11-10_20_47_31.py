n=eval(input())
x=2
y=1
sums=0
while n>0:
    sums=sums+x/y
    y=x
    m=y
    x=y+x
    n-=1
print("%.4f"%sums)
