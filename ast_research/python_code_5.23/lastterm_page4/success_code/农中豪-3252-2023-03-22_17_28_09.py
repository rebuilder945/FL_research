def Fibonacci(num,  n):
    a=num[0]
    b=num[1]
    for i in range(n):
        if i<2:
            end=1
        else:
            end=a+b
            a=b
            b=end
    return end




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


