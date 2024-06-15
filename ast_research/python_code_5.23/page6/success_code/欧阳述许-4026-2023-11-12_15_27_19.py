def a(n):
    if n<=2:
        return n
    return a(n-1)+a(n-2)
n=eval(input())
r=0
for i in range(1,n+1):
    r+=a(i+1)/a(i)
print("%.4f"%r)
