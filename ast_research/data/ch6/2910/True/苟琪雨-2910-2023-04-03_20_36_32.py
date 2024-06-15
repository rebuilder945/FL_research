h=eval(input())
N=eval(input())
a=h
for i in range(N-1):
    b=0.5*a*2
    a=0.5*a
    h=h+b
result=float(h)
print("%.2f"%result)
