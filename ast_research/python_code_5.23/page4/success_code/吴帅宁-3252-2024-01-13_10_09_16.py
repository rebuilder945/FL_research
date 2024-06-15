def Fibonacci(num,n):
    if n==1 or n==2:
        return 1
    else:
        for i in range(3,n+1):
           result=num[i-2]+num[i-3]
           num.append(result)
        return num[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


