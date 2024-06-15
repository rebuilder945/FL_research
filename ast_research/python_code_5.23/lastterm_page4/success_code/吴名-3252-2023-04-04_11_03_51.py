def Fibonacci(m,a):
    i=0
    while 1==1:
        i+=1
        x=num[-1]
        y=num[-2]
        z=x+y
        num.append(z)
        if i>=a:
            return(num[-3])
            break




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


