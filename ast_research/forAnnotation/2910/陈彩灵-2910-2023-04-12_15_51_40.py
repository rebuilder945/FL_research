h=eval(input())
N=eval(input())
s=0
for x in range(N):
    s+=h*(1-0.5)**x
s+=h
print("%.2f"%s)
