def Fibonacci(s,n):
      s=[1,1]
      for i in range(n-2):
           s.append(sum(s[-2: ]))
      return sum(s[-2: ])     
      




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


