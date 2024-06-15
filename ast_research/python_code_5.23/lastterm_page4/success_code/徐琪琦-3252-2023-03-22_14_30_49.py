def Fibonacci(num,n):
    a = 1
    b = 1
    i = 0
    while i < n:
        num.append(a + b)
        c = a                #不可变的参数值，所以不会像列表一样，改了a，c也和a一起变
        a = b
        b = c + b 
        i += 1
    return num[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


