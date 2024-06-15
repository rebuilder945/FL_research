def Fibonacci(num,  n):
    for x in range(n-2):
        a=sum(num)
        num=[num[1],a]
    return a





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


