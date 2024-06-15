def Fibonacci(num,n):
    while n>len(num):
        a=num[-1]
        b=num[-2]
        c=a+b
        num.append(c)
    if n<=len(num):
        an=num[-1]
        return an





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


