n=eval(input())
y=2
x=1
sum=0
for i in range(1,n+1):
    sum+=y/x
    x,y=y,x+y
    print("%.4f"%sum)
