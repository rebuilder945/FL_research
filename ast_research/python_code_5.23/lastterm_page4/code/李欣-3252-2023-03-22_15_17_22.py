def Fibonacci(num,  n):
      if n==1 or n==2:
           Fibonacci(num,n)=1
      else:
            Fibonacci(num,n+1)=Fibonacci(num,n)+Fibonacci(num,n-1)
            return Fibonacci(num,n)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


