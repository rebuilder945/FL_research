def Fibonacci(num,  n):
    for i in range(n-2):
        b = num+num[i+1]
        num.append(b)
    return num[n-2]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


