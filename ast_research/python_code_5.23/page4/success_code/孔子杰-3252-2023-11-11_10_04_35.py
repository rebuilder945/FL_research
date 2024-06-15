def Fibonacci(num,  n):
      for x in range(3,n+1):
           nums.append(num[x-2]+num[x-3])
      return(num[-1])





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


