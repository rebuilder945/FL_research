a=list(eval(input()))
n,m=int(input())
if (n+1)<=len(a):
    for i in range(m):
        a=a+a[n-1]
else:
    print('error')
print(a)
