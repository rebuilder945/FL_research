n=eval(input())
a=2
b=1
sums=0
while n>0:
    sums+= a/b
    m=b
    b=a
    a+=m
    n-=1
print("%.4f"%sums)

