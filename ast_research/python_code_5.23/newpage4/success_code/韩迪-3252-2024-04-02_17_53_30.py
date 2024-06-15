def Fibonacci(num,  n):
      if n==1 or n==2:
           return 1
      else:
           return Fibbonacci(num,n-1)+Fibbonacci(num,n-2)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


