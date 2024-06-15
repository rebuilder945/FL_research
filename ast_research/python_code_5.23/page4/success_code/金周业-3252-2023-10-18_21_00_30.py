def Fibonacci(a,b):
    if b == 1 or b == 2:
        return 1
    return Fibonacci(b-1)+Fibonacci(b-2)





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


