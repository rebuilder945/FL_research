a = eval(input())
n,m = eval(input())
c = len(a)
if n <= c and m <=c:
    del a[n:m]
    print(a)
else:
    print("error")
    







