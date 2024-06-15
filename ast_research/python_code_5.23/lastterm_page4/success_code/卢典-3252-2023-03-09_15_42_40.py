def Fibonacci(num,i):
   for num[i] in num:
         a=eval(num[i-1]+num[i])
         num.append(a)
         return(num[-1])


      




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


