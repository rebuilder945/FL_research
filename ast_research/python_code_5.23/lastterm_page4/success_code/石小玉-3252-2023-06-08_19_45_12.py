def Fibonacci(num,n):
    i=1
    while  i<=n:
        x = num[-2]+num[-1]
        num.append(x)
        i+=1
    result=num[-2]
    return result




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


