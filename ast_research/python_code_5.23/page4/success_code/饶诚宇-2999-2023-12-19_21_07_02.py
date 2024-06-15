a=list(map(str,input().split))
n,m=eval(input())
b=a.copy()
b[n],b[m]=a[m],a[n]
print(b)
