def maxsum(y):
    sum=0
    y.sort(reverse=False)
    for i in range(len(y)):
        if i%2==0:
            sum+=y[i]
    return sum




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


