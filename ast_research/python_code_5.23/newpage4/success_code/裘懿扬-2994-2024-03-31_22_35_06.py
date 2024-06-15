a=input().split(",")
n,m=eval(input())
b=a.copy()
if n<=len(a):
    for i in range(0,m):
        b.append(a[n])
    print(b)
else :
    print('error')


