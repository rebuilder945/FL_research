def Fibonacci(num,n):
      if n==1 or n==2:
           a(n)=1
      else:
            a(n+1)=a(n)+a(n-1)
            return a(n)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


