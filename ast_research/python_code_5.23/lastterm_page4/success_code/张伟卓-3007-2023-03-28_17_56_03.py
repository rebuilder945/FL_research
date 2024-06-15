l=eval(input())
n,m=eval(input())
if n<=m:
    del l[n:m]
    print(l)
else:
    print("error")
