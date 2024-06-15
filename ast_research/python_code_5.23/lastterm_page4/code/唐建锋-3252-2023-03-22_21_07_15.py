def Fibonacci
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        return Fibonacci(n-1)+Fibonacci(n-2)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


