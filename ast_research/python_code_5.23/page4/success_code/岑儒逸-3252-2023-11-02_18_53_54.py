def Fibonacci(ls,x):
    ls1=[]+ls
    if x <= len(ls):
        return ls1[x-1]
    else:
        i=2
        while i<x:
            ls1.append(sum([ls1[-1],ls1[-2]]))
            i+=1
        return ls1[x-1]




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


