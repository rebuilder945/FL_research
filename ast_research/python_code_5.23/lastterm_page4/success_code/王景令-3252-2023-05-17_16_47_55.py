def Fibonacci(num,n):
    ls = num
    for i in range(n):
        ls.append(ls[i+1]+ls[i+2])
    return ls[n-1]





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


