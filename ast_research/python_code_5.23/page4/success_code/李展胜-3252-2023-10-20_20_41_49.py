def Fibonacci(num,n):
      l=[1,1]
      for i in range (n-2):
            l.append(sum(n[-2:]))
      return l[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


