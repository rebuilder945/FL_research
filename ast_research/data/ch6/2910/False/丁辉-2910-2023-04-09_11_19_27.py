h=eval(input())
N=eval(input())
for i in range(N):
    if N==1:
        h=h
    if N>1:
        h=2*h+h*(1/2)
print("%.2f"%h)
