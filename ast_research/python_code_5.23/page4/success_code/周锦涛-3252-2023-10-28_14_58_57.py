n=eval(input())
if n==1 or n==2:
    print('1')
else:
    a,b=1,1
    for i in range(n-2):
        c=a+b
        a=b
        b=c
    print(c)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


