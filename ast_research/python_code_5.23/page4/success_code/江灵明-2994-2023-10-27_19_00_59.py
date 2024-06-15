import math
def p(y,n,m):
    if n!=math.floor(n):
        print("error")
    else:
        if n>=-len(y) and n < len(y):
            x = y[n]
            for i in range(m):
                y.append(x)
            print(y)
        else:
            print("error")
d = list(eval(input()))
n,m = eval(input())
p(d,n,m)
