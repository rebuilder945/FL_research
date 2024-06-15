def Fibonacci(num,n):
      n=[1,1]
      for i in range (n):
            n.append(sum(n[-2:]))




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


