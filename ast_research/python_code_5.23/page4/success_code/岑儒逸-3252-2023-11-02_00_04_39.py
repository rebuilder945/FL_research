def Fibonacci(lsit,n):
    ls1=[]
    ls1.append(lsit[0])
    ls1.append(lsit[1])
    if n ==1:
        return ls1[0]
    elif n==2:
        return ls1[1]
    else:
        for i in range(1,n-4):
            ls1.append(ls1[i] + ls1[i+1])
        return ls1[n-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


