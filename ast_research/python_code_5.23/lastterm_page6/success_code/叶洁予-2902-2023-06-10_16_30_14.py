n=int(input())
a=2
b=1
s=0
for x in range(1,n+1):
    s=s+a/b
    c=b
    b=a
    a=a+c
print("%.4f"%s)

