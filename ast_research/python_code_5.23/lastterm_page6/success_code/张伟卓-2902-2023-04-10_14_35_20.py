a=eval(input())
x=2
y=1
sum=0
while a>0:
    sum=sum+x/y
    
    y=x
    x=x+y
    a-=1
print("%.4f"%sum)
