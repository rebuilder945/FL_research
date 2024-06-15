def Fibonacci(m,n):
    a=m[0]
    b=m[1]
    for x in range(n-2):
        if x%2==0:
            a=a+b
        else:
            b=a+b
    if n%2==1:
        return a
    else:
        return b





num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


