h=eval(input())
N=eval(input())
n=1
x=h
while n<N:
    x += 2*h*(0.5)**n
    n+=1
print("%.2f"%x)
