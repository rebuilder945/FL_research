def Fibonacci(num,  n):
    for i in range(0,n+1):
        a = num[0+i]+num[1+i]
        num.append(a)
    return(num[n-1])




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


