def Fibonacci(num,n):
      last=num[0];
      now=num[1];
      a=1
      for i in range(n):
           if i<2:
              a=1
           else:
                 a=last+now
                 last=now
                 now=a
       return a





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


