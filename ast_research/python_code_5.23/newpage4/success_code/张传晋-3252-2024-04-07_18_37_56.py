def Fibonacci(num,n):
    s = 0
    for i in range(n-2):
        yuansu = num[s] + num[s+1]
        s+=1
        num.append(yuansu)
    return num[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


