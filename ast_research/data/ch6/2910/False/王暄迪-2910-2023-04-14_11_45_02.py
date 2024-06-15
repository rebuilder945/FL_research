h=float(input())
N=int(input())
m=h
for i in range(N-2):
    m+=0.5**i*h
print("%.2f"%(m))
