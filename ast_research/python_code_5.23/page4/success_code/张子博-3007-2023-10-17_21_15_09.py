p=eval(input())
print(p)
n,m=eval(input())
if n<=m:
    del p[n:m]
    print(p)
else:
    print("error")

