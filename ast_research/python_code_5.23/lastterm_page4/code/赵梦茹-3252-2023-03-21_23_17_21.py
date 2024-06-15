def Fibonacci(num, n):
      last=num[0];
      now=num[1];
      fibnext=1
      for i in range(n):
           if i<2:
              a=1
           else:
                 fibnest=last+now
                 last=now
                 now=fibnest
       return a





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


