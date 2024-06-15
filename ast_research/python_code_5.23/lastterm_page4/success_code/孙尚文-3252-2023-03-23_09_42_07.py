def Fibonacci(num,n):
    a=[]
    for x in range(2,n):
        y=num[x-2]+num[x-1]
    a=num.append(y)
    return a  

    




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


