def Fibonacci(n):
    lst=[1,1]
    if n<=2:
        return 1
    else:
        for i in range(n-2):
            a=lst[-1]+lst[-2]
            lst.append(a)
    return lst[-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


