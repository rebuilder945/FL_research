def Fibonacci_number(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return Fibonacci_number(n-1)+Fibonacci_number(n-2)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


