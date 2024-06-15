a = []
def Fibonacci(num,n):
    for i in num:
        m = num[i] + num[i+1]
        a.append(m)
    b = a[n-1]
    return b




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


