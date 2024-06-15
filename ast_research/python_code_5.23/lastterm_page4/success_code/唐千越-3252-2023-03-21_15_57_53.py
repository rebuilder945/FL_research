def Fibonacci(a,b):
    x=a[-1:-2]
    y=a[-2:-3]
    z=x+y
    a.append(z)
    for i in range(a):
        b=a[i]
    return b
     





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


