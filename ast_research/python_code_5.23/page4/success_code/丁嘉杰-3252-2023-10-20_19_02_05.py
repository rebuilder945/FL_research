def Fibonacci(num,n):
    for i in range(3,n+1):
        F=num[i-3]+num[i-2]
        num.append(F)
    return num(n)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


