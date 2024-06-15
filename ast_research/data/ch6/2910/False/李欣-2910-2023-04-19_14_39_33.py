h=float(input())
N=int(input())
total=h
while N>0:
    h=0.5*h
    total+=2*h
    N+=-1
print("%.2f"%total)
