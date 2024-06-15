a=1  b=0  c=1
def Fibonacci(num,n)
      for i in range (n)
          c=a+b
          a=c
          b=a
return c
          




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


