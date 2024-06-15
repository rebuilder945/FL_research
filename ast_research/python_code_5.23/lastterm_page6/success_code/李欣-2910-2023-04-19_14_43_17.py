h=float(input())
N=int(input())
total=0
while N>0:
    total+=h
    h=0.5*h
    N+=-1
print("%.2f"%total)
