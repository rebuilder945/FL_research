def Fibonacci(num,n):
    f=0
    for num in num:
        s=num[f+1]+num[f]
        num.append(s)
        f+=1
    return Fibonacci[n]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


