h=eval(input())
N=eval(input())
H=h
if N==1:
    print("%.2f"%H)
else:
    for i in range(1,N-1):
        a=h*0.5
        b=a*2
        H+=b
print("%.2f"%H)

