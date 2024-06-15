h=eval(input())
N=eval(input())
x=h
while N>1:
    h*=0.5
    x+=2*h
    N-=1
print("%.2f"%x)
