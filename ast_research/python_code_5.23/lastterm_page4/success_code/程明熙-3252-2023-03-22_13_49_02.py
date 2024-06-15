def Fibonacci(num,n):
    last1=num[:1]
    last2=num[1:2]
    for i in range(n):
      c=last1+last2
      last1,last2=last2,ast1+last2
    return c




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


