a=eval(input())
n,m=eval(input())
if n>m or n==m:
    print("error")
elif n not in range(len(a)) or m not in range(len(a)):
    print("error")
else:
    for i in range(n,m):
        del a[i]
    print(a)





