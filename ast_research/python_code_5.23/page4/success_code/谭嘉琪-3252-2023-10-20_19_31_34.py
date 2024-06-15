def Fibonacci(num,n):
      a=eval(num[0:1])
      b=eval(num[1:])
      for i in range (n-1):
           a,b=b,a+b
      return b

           




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


