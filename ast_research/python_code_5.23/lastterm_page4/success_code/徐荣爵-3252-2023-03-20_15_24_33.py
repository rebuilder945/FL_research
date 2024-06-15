def Fibonacci(num,  n):
    for i in range(n-2):
        m1 = int(num[i])
        m2 = int(num[i+1])
        m = m1+m2
        num.append(m)
    return num.pop()




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


