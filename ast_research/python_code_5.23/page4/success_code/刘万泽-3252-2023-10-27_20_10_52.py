def Fibonacci(num,n):
      for i in range(n):
           b=num[i]+num[i+1]
           num.append(b)
           if i ==n-2:
              break
      return num[n-1] 
       




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


