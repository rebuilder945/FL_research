def F(num,n):
    an-1,an = num
    for i in range(n-2):
        an+1 = an-1 + an
        an-1 = an
        an = an+1
    return an+1




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


