def Fibonacci(num,n):
    last=num[0]
    now=num[1]
    fibonacci=last+now
    last=now
    now=fibonacci
    return fibonacci




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


