def Fibonacci(ls,n):
    for x in range(n-2):
        ls.append(ls[x]+ls[x+1])
    a = ls.pop()
    return a




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


