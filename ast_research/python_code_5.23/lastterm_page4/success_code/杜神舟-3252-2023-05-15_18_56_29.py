def Fibonacci(num,  n):
    for x in range(n):
        bb=num[0+x]+num[1+x]
        num.append(bb)
        cc=num[n-2]
    return cc





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


