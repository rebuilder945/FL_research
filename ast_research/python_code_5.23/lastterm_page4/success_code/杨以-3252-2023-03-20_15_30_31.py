def Fibonacci(num,n):
    a=((1+5**0.5)/2)**n
    b=((1-5**0.5)/2)**n
    f=(a-b)/(5**0.5)
    f=int(f)
    return f




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


