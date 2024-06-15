def Fibonacci(num,n):
      n=[1,1]
      for i in range (n-2):
            n.append(sum(n[-2:]))
            return n[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


