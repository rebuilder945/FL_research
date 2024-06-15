h=float(input())
N=int(input())
m=h
for i in range(N-1):
    m+=h
    h=0.5*h
print("%.2f"%(m))
