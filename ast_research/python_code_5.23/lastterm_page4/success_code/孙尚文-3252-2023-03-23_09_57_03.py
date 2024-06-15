def Fibonacci(num,n):
    a=[]
    for x in range(n):
        y=num[x-1]+num[x-2]
    a=num.append(y)
    return a  

    




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


