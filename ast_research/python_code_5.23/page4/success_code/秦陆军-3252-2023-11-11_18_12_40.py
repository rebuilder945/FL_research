def Fibonacci(num,n):
     if len(num)<n:
        s = num[-1]+num[-2]
        num.append(s)
     return num[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


