def Fibonacci(x,y):
   x=[1,1]
   for i in range(y):
      a=x[i]+x[i+1]
      x.append(a)
   return(x[y])




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


