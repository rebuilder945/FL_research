def Fibonacci(a,n):
    if n>len(a):
        for i in range(n-len(a)):
            c = a[-1]+a[-2]
            a.append(c)
        return a[n-1]
    else:
        return a[2]
a = eval(input())
b = [1,1]
d = 0
for i in range(3,a+3):
    d += Fibonacci(b,i)/Fibonacci(b,i-1)
print("%.4f"%d)

