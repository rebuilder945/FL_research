h=eval(input())
N=eval(input())
H=h
if N>1:
    for i in range(N-1):
        H=H+2*((1/2)**i)*h
    print("%.2f"%H)
if N==1:
    print("%.2f"%h)
