a = eval(input())
a = list(a)
n,m = eval(input())
if n>(len(a)-1):
    print("error")
else:
    b = a[n]
    b1 = ([b]*m)
    print(a+b1)
