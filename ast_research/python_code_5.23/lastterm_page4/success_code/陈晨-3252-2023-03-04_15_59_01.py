def Fibonacci(num,  n):
    k=2
    while k!=n:
        num.append(num[k-2]+num[k-1])
        k+=1
    return num[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


