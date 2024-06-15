a = eval(input())
n,m = map(int,input().split(","))
if n < len(a) and m < len(a):
    del a[n:m]
    print(a)
else:
    print("error")    

