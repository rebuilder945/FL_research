def Fibonacci(num,n):
    for i in range(0,n-2):
        a=num[i]+num[i+1]
        num.append(a)
        a=num[n]
        return(a)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


