def Fibonacci(num,n):
      n1=1
      n2=0
      current=1
      for x in range(2,n+1):
           current=n2+n1
           n2=n1
           n1=current

return current




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


