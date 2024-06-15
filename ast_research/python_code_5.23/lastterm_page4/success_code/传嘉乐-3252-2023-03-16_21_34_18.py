def Fibonacci(num,n):
   a=b=num=1
   while n>2:
      a=b
      b=num
      num=a+b
      num-=1
   return num




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


