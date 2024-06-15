def Fibonacci(num, n):
        while len(num) < n:
              num.append(num[-1] + num[-2])
    return num[n-1] 




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


