def Fibonacci(num:list,n):
    for i in range(3,n+1):
        num.append(num[i-1-1]+num[i-1-2])
    return num[-1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


