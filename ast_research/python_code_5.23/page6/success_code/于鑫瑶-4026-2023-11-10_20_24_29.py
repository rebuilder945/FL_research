n=eval(input())
x=2
y=1
while n>0:
    sums=sums+x/y
    m=y
    y=x
    x=m+x
    n-=1
print("%.4f"%sums)
