def Fibonacci(num,  n):
     for x in range(1,n):
          b=num[x]+num[x-1]
          num.append(b)
     return(num[n-1])




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


