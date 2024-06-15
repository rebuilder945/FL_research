def lst(a):
    b = a[n]
    if n < 0:
        if -n <= len(a):
            a.pop(n)
            for i in range(m):
                a.append(b)
            print(a)
        else:
            print('error')
    else:
        if n < len(a):
            a.pop(n)
            for i in range(b):
                a.append(b)
            print(a)
        else:
            print('error')
a =list(eval(input()))
n,m = eval(input())
lst(a)

