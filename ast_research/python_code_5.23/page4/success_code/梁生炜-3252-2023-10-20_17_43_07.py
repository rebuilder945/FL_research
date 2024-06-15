def Fibonacci(x,y):
   for i in range(y):
      a=x[i]+x[i+1]
      x.append(a)
   return(x[y-1])




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


