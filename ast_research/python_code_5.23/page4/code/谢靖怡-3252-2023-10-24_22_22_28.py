def Fibonacci(num,n):
     for i in range(n-2):
         a=num[-1]
         b=num[-2]
         c=a+b
         num.append(c)
      return c




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


