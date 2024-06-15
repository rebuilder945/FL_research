a=int(input())
b=2
c=1
while a >0:
    sums=2
    sums+=b/c
    x=c
    c=b
    b+=c
    a-=1
print("%.4f"%sums)
