n=int(input())
x=2
y=1
sum=0
for i in range(n):
    sum=sum+x/y
    m=y
    y=x
    x=y+m
    n-=1
print("%.4f"%sum)
    
