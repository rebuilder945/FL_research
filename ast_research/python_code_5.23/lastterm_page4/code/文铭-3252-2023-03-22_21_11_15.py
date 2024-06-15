def Fibonacci(num,  n)
      for i in range(n-2):
            a = sum(num[-2:])
            num.append(a)
      p = num.pop()
      return p




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


