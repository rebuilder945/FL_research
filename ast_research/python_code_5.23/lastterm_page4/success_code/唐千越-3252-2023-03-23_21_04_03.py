def Fibonacci(a:list,b):
      for x in range(3,n+1):
           a.append(a[x-1-1]+a[x-1-2])
      return  a[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


