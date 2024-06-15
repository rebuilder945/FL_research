l = eval(input())
n,m = eval(input())
if n < 0:
    n = len(n)+n
    if n-1 >len(l):
        print("error")
    else:
        a = l[n]
        b = l.count(a)
        for i in range(b):
            l.append(a)
        print(l)
