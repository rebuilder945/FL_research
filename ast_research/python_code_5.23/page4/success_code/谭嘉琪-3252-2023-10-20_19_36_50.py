def Fibonacci(num,n):
      a=int(num[0:1])
      b=int(num[1:])
      for i in range (n-1):
           a,b=b,a+b
      return b

           




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


