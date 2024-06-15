def Fibonacci(a,b):
    for x in range(b-2):
        c=a[-1]+a[-2]
        a.append(c)        
    return(c)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


