h=int(input())
N=int(input())
s=h
for x in range(N-1):
    s+=h*0.5**x
print("%.2f"%s)

