def ss(n):
    if n > 0:
        for i in range(2,n):
            if n % i == 0:
                return 0
    return 1

def hw(n):
    a = input()
    m = a[::-1]
    if m ==a:
        return n

n = eval(input())
if n <=1:
    print("illegal input")
elif n - int(n) > 0:
    print("illegal input")
else:
    n = int(n)
    b = []
    for i in range(2,n):
        if ss(i) and hw(i) == i:
            b.append(i)
    for i in range(len(b)):
        print(b[i],end = " ")
