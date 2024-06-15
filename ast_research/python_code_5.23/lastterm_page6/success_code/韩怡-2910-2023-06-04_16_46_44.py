h=eval(input())
N=eval(input())
H=h
if N==1:
    print("%.2f"%H)
else:
    for i in range(1,N-1):
        H+=h*0.5
print("%.2f"%H)

