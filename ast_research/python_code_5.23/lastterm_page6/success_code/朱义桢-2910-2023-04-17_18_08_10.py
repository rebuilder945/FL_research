h=eval(input())
N=eval(input())
l=h
if N==1:
    print("%.2f"%l)
else:
    for i in range(1,N):
        a=2*h*0.5**i
        l+=a
    print("%.2f"%l)
