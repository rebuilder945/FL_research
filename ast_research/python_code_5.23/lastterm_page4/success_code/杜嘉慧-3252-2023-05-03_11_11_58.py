def Fibonacci(num,n):
      for i in range(2,n):
           num.append(num[-1]+num[-2])
      return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


