a=eval(input())
n,m=eval(input())
b=len(a)
if n>(b-1)  or n>m:
    print("error")
elif n==m:
    del a[n]
    print(a)
elif m>(b-1):
    for x in range(n,b):
        del a[x]
    print(a)

else:
    for x in range(n,m):
        del a[x]
    print(a)



