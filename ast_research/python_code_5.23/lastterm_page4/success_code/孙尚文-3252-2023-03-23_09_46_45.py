def Fibonacci(num,n):
    a=[]
    for x in range(n):
        y=num[x]+num[x+1]
    a=num.append(y)
    return a  

    




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


