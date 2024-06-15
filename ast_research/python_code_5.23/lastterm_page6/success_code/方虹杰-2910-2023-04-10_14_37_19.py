h=float(input())
N=int(input())
s=h
preh=h
for i in range(1,N):
    s+=preh
    preh=preh/2
print("%.2f"%s)

