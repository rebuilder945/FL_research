h=int(input())
N=int(input())
s=h
for i in range(N):
    h=h*0.5
    s=s+h
print("%.2f"%s)
