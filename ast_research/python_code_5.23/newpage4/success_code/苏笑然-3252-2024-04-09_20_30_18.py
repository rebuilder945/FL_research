def Fibonacci(num,n):
    if n>len(num):
        a=num[-1]
        b=num[-2]
        c=a+b
        num.append(c)
    print(num[-1])




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


