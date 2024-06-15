def Fibonacci(num,n):
   i=2
   a1=1
   a2=1#a1是current前第二个数，a2是current前一个数
   current=2
   if n==3:
      return current
   else:
      while  i != n:
         i+=1
         current=a1+a2
         num.append(current)
         a1=current
         a2=a1
   return current
num=[1,  1]
n=int(input())
print(Fibonacci(num,n))




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


