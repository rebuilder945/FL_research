def Fibonacci(num, n):
      for x in range(n):
      shu = num[x]+num[x+1]
      num.append(shu)
      if(x+1)==(n-2):
        return shu





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


