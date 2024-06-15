def Fibonacci(num,n):
      k=[1,1]
      for i in range(n-2):
            k.append(sum(k[-2:]))
      return k[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


