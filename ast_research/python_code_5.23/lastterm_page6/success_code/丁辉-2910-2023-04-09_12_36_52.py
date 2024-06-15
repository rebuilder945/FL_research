h=eval(input())
N=eval(input())
H=0
if N>1:
    for i in range(N):
        H=H+2*((1/2)**i)*h
    print("%.2f"%H)
if N==1:
    print("%.2f"%h)
