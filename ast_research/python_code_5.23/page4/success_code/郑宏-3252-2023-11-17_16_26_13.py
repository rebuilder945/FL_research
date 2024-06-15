def Fibonacci(num,  n):
    a=num[0]
    b=num [1]
    for i in range(n-2):
        a+=b
        b=a
    return (a)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


