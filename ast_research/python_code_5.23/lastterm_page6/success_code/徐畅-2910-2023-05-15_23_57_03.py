h=eval(input())
n=eval(input())
heigh=h
while n!=1:
    h=0.5*h
    heigh=heigh+h*2
    n=n-1
print("%.2f"%heigh)
