def Fibonacci(num,n):
      for i in range(n):
            num.append(num[-1]+num[-2])
      n=num[n-1]
      return n




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


