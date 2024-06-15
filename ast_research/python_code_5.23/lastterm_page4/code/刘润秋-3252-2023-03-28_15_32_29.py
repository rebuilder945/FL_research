def Fibonacci(num,n):
      a=num[0];
      b=num[1];
      for i in range(n):
      f=a+b;
      a=b; 
      b=f;
      return a;




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


