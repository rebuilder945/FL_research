a = eval(input())
n,m = eval(input())
if n < 0 or m > len(a):
    print("error")
else:
    if n > m:
        print("error")
    else:
        del a[n:m]
        print(a)
