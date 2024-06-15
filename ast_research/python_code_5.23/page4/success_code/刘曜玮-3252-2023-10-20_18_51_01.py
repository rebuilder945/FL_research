def Fibonacci(num,n):
    x=2
    while x!=n:
        b=num[-2]+num[-1]
        num.append(b)
        x+=1
    return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


