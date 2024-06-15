def fibonacci(n):
      if n <= 0: 
          return "Invalid input"
      elif n == 1: 
           return 0 
      elif n == 2: 
           return 1 
      else: a = 0 
      b = 1 
      for i in range(3, n+1): 
           c = a + b 
           a = b 
           b = c 
           return b




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


