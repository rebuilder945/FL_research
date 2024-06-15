def Fibonacci(num,n):
    i=1
    for x in range(n-2):
        a=num[i-1]+num[i]
        i=i+1
        num.append(a)
    return a




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


