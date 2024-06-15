def Fibonacci(num,n):
    a=(1/(5**0.5))*(((1+5**0.5)/2)**n-((1-5**0.5)/2)**n)
    num.append(a)
    return("%.d"%(a))
   
  



      




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


