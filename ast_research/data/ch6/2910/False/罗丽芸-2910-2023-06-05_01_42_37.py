h=eval(input())
n=eval(input())
s=0
for i in range(n,n+1):
    if n==1:
        s+=h
    else:
        s+=2*h
    h=h/2
print("%.2f"%s)
