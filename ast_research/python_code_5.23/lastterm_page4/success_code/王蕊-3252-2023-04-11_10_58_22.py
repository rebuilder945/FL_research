def Fibonacci(num,n):
    i=len(num)
    n=eval(n)
    if n<i:
        z=num[-1]+num[-2]
        num.append(z)
        i+=1 




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


