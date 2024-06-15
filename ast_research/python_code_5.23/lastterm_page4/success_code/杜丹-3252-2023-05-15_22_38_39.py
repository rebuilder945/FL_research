def Fibonacci(n):
      if n<=0:
         return
      elif n==1:
         return 1
      else:
         return Fibonacci(n-1)+Fibonacci(n-2)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


