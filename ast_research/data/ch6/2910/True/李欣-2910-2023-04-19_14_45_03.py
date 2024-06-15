h=float(input())
N=int(input())
total=h
while N-1>0:
    total+=h
    h=0.5*h
    N+=-1
print("%.2f"%total)
