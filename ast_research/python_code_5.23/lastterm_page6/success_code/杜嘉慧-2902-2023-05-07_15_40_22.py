n=int(input())
x=2
y=1
sums=0
while n>0:
    sums+=x/y
    m=y
    y=x
    x=x+m
print("%.4f"%sums)

