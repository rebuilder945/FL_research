a=list(eval(input()))
n,m=eval(input())
if n>len(a):
    print('error')
else:
    a.append(a[n+1]*m)
    print(a)
