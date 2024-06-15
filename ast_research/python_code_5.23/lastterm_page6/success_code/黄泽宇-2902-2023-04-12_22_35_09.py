x,y=2,1
n=eval(input())
sum=0
while n>0:
    sum=sum+x/y
    m=y
    y=x
    x+=m
    n-=1
print("%.4f"%sum)
