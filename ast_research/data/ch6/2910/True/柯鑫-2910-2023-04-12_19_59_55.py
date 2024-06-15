h=eval(input())
n=eval(input())-1
H=h
if n==1:
    print("%.2f"%h)
else:
    while n>0:
        H+=h*0.5*2
        h*=0.5
        n-=1
    print("%.2f"%H)
