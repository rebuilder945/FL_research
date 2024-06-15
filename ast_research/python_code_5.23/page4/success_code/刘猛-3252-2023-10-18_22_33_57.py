def Fibonacci(num,  n):
  num = [1,1,2]
  for i in range(3,10000):
    x = num[i-1]+num[i-2]
    num.append(x)
  a = num[n-1]
  return a
      




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


