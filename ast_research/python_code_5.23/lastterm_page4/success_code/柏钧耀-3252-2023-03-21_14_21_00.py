def Fibonacci(num,  n):
   
   for i in range(2,n):
       num1=num[i-1]+num[i-2]
       num.append(num1)
   return num[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


