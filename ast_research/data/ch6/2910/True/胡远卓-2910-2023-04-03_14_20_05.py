h=eval(input())
n=eval(input())
res=-1.0*h
for i in range(n):
    res+=2*h
    h/=2
print("%.2f"%res)
