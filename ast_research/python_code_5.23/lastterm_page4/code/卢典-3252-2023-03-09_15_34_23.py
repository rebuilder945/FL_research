def Fibonacci(num,n):
   for 1<=i<n:
   num.append(num[i-1]+num[i])
   return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


