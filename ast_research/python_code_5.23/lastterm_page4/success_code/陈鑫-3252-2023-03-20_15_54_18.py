def Fibonacci(num,n):
    f=0
    for num in num:
        num[f+2]=num[f+1]+num[f]
        num.append(num[f+2])
        f+=1
    return Fibonacci[n]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


