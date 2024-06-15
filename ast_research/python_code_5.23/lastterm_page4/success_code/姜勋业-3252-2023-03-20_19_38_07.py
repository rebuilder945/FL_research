def  Fibonacci(a,b):
       c,d=a
       for i in range(b-2):
            e=c+d
            c=d
            d=e
       return e
       




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


