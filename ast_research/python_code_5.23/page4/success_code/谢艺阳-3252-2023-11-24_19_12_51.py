def Fibonacci(num,n):
   if(n<2):
       return 1
   for i in range(2,n):
        num.append(num[i-1]+num[i-2])
   return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


