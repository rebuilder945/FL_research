n=int(input())
a=2
b=1
c=0
for x in range(1,n+1):
    c=c+a/b
    a,b=a+b,a
print("%.4f"%c)

