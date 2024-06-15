def Fibonacci(num,n): 
    for i in range(n):
        if i>=2:
            a=i-1
            b=i-2
            numn=num[a]+num[b]
            num.append(numn)
        else:
            continue
    return numn




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


