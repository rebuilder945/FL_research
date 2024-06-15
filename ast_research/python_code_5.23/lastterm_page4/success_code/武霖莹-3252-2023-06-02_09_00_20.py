def Fibonacci(num,  n):
    for i in range(n-2):
        b = num[-1] + num[-2]
        num.append(b)
    return(num[-1])




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


