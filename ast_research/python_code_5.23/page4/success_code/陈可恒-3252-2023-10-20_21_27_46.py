def Fibonacci(a,b):
    while b-2:
        s = num[-1]+num[-2]
        a.append(s)
        b=b-1
    return a[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


