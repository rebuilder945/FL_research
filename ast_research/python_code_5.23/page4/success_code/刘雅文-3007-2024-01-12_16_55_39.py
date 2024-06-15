a=eval(input())
n,m=eval(input())
if m<=len(a) and n<=m:
    b=a[:n]+a[m:]
    print(b)
else:
    print('error')
