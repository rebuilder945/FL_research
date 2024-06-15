def Fibonacci(num,n):
    num=[x+y for x in num[:] for y in num[1:] for i in range(n) num.append(x+y)]
    return num[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


