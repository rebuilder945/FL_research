def  Fibonacci(a,b):
       c=1
       d=1
       for i in range(b-2):
            c=c+d
            d=c+d
       return d
       




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


