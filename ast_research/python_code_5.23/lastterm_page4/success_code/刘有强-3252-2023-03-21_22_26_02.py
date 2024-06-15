def Fibonacci(num,n):
    lastdo=0
    first=1
    second=1
    if n <= 2:
        lastdo=1
    else:
        for i in range(n-2):
                lastdo=first+second
                first=second
                second=lastdo
    return lastdo




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


