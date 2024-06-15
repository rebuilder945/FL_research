a=list(eval(input()))
n,m=eval(input())
b=len(a)
c=0
if -b<=n<b-1 and m>0:
    c=a[n]
    for i in range(m):
        a.append(c)
    print(a)
else:
    print('error')
