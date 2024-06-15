h=eval(input())
n=eval(input())
s=h
for i in range(n+1):
    s=s+0.5*s
print("%.2f"%s)
