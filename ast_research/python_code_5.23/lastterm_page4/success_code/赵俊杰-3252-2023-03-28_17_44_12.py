def fibonacci(num,n):
      for x in range(n-2):
          num.append(num[-1]+num[-2])
          return num[-1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


