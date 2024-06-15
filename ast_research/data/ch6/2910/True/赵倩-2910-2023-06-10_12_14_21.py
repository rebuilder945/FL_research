h=int(input())
N=int(input())
s=h
for i in range(N-1):
    s=0.5*s
    h+=s*2
print("%.2f"%h)








