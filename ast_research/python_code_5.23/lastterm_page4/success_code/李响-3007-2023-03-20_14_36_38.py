a = eval(input())
n,m = eval(input())
b = len(a)
if  n <= m <= b-1:
    del a[n:m]
    print(a)
else :
    print("error")
