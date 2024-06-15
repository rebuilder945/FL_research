def Fibonacci(a,b):
    for i in range(b-2,b-2):
        a=a.append(a[-1]+a[-2])
    print(a[-1])




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


