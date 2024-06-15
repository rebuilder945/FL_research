h=eval(input())
n=eval(input())
s=h
k=h
for i in range(n+1):
    s=s+k
    k=0.5*k
print("%.2f"%s)
