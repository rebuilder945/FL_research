n=eval(input())
b=[]
def fibonacci(n):
    a=[1,1]
    for i in range(2,n):
        a.append(a[-1]+a[-2])
    return a[-1]
for i in range(1,n+1):
    b.append(fibonacci(i+2)/fibonacci(i+1))
print("%.4f"%sum(b))
