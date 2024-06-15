def lst(a):
    if n < 0:
        if -n <= len(a):
            b = a[n]
            for i in range(m):
                a.append(b)
            print(a)
        else:
            print('error')
    else:
        if n < len(a):
            b = a[n]
            for i in range(m):
                a.append(b)
            print(a)
        else:
            print('error')
a =list(eval(input()))
n,m = eval(input())
lst(a)

