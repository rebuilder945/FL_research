def Fibonacci(num,n):
    ls = num
    for i in range(n):
        ls.append(ls[i]+ls[i+1])
    return ls[n-1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


