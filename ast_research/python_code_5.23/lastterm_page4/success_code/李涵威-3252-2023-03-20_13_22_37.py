visited = {}
def Fibonacci(num,n):
    if n == 1 or n == 2:
            return num[n-1]
    else:
        if n in visited.keys():
            return visited[n]
        else:
            r = Fibonacci(num,n-1) + Fibonacci(num,n-2)
            visited[n] = r
            return r




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


