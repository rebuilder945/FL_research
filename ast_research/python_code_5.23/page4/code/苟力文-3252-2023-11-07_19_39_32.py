def Fibonacci(num,n):   
    a=num[0]
    b=num[1]
    c=1
    for i in range(n):
        if  i<2:
            Fibonacci=1
        else: 
            c=a+b
            a=b
            b=c
         returm   c




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


