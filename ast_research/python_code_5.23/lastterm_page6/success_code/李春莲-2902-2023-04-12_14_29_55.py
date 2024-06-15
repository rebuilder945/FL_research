n=eval(input())
x=1
y=2
sum=2
for i in range(1,n+1):
    sum+=y/x
    x,y=y,x+y
    print("%.4f"%sum)
