def Fibonacci(num,n):
    for x in num:
        num[x+2]=num[x+1]+num[x]
        return num
    return Fibonacci[n]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


