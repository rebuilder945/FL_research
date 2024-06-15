a=eval(input())
n,m=input()
if n>m or n==m:
    print("error")
else:
    for i in range(n,m):
        del a[i]
    print(a)





