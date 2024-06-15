def Fibonacci(m,l):
    a=m[0]
    b=m[1]
    if l-2>=0:
        for x in range(l-2):
            d=a+b
            a=b
            b=d
    if l-2<0:
        d=1        
    return d        




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


