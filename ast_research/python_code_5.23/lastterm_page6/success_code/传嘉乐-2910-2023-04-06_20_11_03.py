h=eval(input())
n=eval(input())
x=2*h
while n>1:
    n-=1
    h+=x/2
    x=x/2
print("%.2f"%h)
