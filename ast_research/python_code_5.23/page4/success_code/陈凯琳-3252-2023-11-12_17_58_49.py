def Fibonacci(num,n):
    i=0
    while i<(n-2):
        a=num[-1]+num[-2]
        num.append(a)
        i+=1
    return num[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


