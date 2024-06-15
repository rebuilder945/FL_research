l = input().split()
n,m = eval(input())
if n < 0:
    n = len(l)+n
if n-1 >len(l):
        print("error")
else:
    a = l[n]
    for i in range(m):
        l.append(a)
    print(l)
