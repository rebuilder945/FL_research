h=float(input())
N=int(input())
m=h
for i in range(N-2):
    m+=h
    h=0.5*h
print("%.2f"%(m))
