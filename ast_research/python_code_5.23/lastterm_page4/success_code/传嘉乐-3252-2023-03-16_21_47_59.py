def Fibonacci(num,n):
   a=b=num=1
   if n<3:
     Fibonacci(num,n)==1,n 
   else:
      while n>2:
         a=b
         b=num
         num=a+b
         n-=1
      return num




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


