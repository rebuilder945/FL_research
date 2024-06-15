def Fibonacci(num,n):
       last=1
       now=1
       f=1
       for i in range(n):
            if i<2:
               f=1
            if i>=2:
               f=last+now
               last=now
               now=f
       return f




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


