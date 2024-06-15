def Fibonacci(num,n):
      a=num[0];
      b=num[1];
      f=1;
      for i+1 in range(n):
            if i+1<3:
                    f=1
            else:
                  f=a+b
                  a=b
                  b=f
      return f




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


