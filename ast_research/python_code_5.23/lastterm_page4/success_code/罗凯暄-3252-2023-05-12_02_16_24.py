def Fibonacci(num, n):
     if n <= 0:
          return None
     elif n <= len(num):
          return num[n-1]
     else:
          fib = Fibonacci(num,n-1)+Fibonacci(num,n-2)
          num.append(fib)
          return fib




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


