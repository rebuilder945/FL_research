n,m,l = eval(input())
a = []
for b in range(1,m+1):
    x = n + (b-1)*l
    a.append(x)
    if len(a) == m:
        print(a)
    else:
        pass

