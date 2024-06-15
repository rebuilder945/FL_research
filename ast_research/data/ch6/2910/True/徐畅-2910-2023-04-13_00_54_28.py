h=eval(input())
N=eval(input())
a=h
b=h
if N==1:
    a=h
else:
    for i in range(2,N+1):
        b=b*(1/2)
        a=a+ 2*b
print("%.2f"%a)
