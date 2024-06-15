def maxsum(lie):
    lie.sort()
    n=len(lie)
    op=[]
    p=int(n/2)
    for a in lie[p:n+1]:
        op.append(a)
    return sum(op)




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


