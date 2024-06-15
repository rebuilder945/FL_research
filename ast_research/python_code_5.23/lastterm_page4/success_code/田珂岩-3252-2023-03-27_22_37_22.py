def Fibonacci(num,n):
    ls = num
    for i in range(2,n):
        ls.append(ls[-1]+ls[-2])
    return ls[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


