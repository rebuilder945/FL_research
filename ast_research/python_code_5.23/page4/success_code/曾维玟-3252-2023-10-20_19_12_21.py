def Fibonacci(num, n):
       a,b = num
       for i in range(n-1):
             a, b = b, a + b
       return a,b




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


