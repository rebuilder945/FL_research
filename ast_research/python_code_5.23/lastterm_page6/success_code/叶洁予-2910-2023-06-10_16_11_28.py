h=float(input())
N=int(input())
s=h
for x in range(1,N):
    s=s+2*h*(0.5)**x
print("%.2f"%s)

