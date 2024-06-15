def Fibonacci(num,  n):
    for x in range(n-2):
        a=num[x]+num[x+1]
        num+=[a]
    return num[n]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


