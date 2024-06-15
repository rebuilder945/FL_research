def Fibonacci(n):
    
   if n <= 0:
      return None
   if n == 1 or n == 2:
     return 1
   else:
      return fibonacci(n - 1) + fibonacci(n - 2)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


