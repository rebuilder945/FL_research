def fibonacci(num,nm):   
    a=num[0]
    b=num[1]
    c=1
    for i in range(n):
        if  i<2:
            c=1
        else: 
            c=a+b
            a=b
            b=c
    print(c)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


