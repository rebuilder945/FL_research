h=eval(input())
n=eval(input())
s=h
k=h
for i in range(n-1):
    k=k*0.5
    s=s+2*k
print("%.2f"%s)
