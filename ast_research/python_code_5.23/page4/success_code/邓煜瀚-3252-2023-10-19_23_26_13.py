def Fibonacci(a,b):
    for i in range(b-2):
        c=a[-2]
        d=a[-1]
        a=a.append(c+d)
    print(a[-1])
    




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


