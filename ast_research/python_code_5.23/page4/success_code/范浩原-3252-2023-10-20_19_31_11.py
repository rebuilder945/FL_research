def Fibonacci(num,n):
  i=0
  while i<=n:
      x=num[-2]+num[-1]
      num,append(x)
      i=i+1
  result=num[n-1]
  return result




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


