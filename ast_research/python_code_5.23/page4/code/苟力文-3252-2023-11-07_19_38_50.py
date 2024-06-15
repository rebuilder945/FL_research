def Fibonacci(num,n):   
    a=num[0]
    b=num[1]
    Fibonacci=1
    for i in range(n):
        if  i<2:
            Fibonacci=1
        else: 
            Fibonacci=a+b
            a=b
            b=Fibonacci
         returm   Fibonacci




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


