def Fibonacci(num,n):
       t=0
       while t<=n-3:
                a=num[t]+num[t+1]
                num.append(a)  
                t+=1
       return  num[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


