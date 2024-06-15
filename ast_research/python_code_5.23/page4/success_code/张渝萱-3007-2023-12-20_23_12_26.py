a = eval(input())
n, m = eval(input())
length = int(len(a))
if m > length:
    print("error")
elif n > length:
    print("error")
elif n <= m:
    count = m-n
    while count > 0:
        del a[m-1]
        count -= 1
    print(a)
elif n > m:
    t = m
    m = n
    n = t
    count = m - n
    while count > 0:
        del a[m]
        count -= 1
    print(a)


