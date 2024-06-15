a=eval(input())
n,m=eval(input())
b=len(a)
if n>(b-1) or m>(b-1) or n>=m:
    print("error")
else:
    for x in range(n,m):
        del a[x]
    print(a)



