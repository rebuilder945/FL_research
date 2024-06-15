def Fibonacci(num,n):
    last=num[0]
    now=num[1]
    fibonacci=1
    for i in range(n):
        if i<2:
            fibonacci=1
        else: 
            bonacci=last+now
            last=now
            now=fibonacci
            return fibonacci




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


