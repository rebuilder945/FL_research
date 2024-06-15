h=eval(input())
n=eval(input())-1
a=h
if n==1:
    print("%.2f"%a)
else:
    while n>0:
        a+=h*0.5*2
        h*=0.5
        n-=1
    print("%.2f"%a)

