h=float(input())
N=int(input())
H=h
for i in range(N-1):
    h=h/2
    H+=h*2
print("%.2f"%H)


