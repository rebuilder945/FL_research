n=int(input())
a=2
b=3
d=1
f=2
sum = 0
for i in range(n):
    sum+=a/d
    c=a+b
    a=b
    b=c
    h=d+f
    d=f
    f=h
print("%.4f"%sum)



