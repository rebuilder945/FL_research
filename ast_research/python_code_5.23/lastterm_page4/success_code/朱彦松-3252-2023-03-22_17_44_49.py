def Fibonacci(ls1, n):
    for i in range (n-2):
        new=ls1[-1]+ls1[-2]
        ls1.append(new)
    return ls1[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


