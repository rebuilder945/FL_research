def Fibonacci(num,n):
      a=1
      b=1
      for i in range (n):
           a,b=b,a+b
      return b

           




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


