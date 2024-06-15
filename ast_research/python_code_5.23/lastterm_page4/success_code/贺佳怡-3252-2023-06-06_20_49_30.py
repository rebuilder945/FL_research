def Fibonacci(a,b):
       while b>2:
              c=a[-1]+a[-2]
              a.append(c)
              b-=1
       return a[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


