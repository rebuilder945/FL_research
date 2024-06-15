a = list(eval(input()))
n,m = eval(input())
if m < len(a) and n < len(a):
    del a[n:m]
    print(a)
if m > len(a) or n > len(a):
    print("error")

