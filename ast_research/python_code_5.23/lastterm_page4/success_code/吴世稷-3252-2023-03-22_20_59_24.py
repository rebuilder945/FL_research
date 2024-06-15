def Fibonacci(num:list,  n:int):
    for a in range (n+1):
        if a > 2:
            b = num[a-2] + num[a-3]
            num.append(b)
    r = num[n-1]
    return r
num  =  [1,  1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


