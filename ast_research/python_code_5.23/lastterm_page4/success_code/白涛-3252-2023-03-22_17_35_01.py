def Fibonacci(a,b):
    i=0
    while i<b-2:
        a.append(a[-1]+a[-2])
        i+=1
    c=a[-1]
    return(c)  
    
    




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


