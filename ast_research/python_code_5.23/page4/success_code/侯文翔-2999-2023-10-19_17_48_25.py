a=list(map(str,input().split()))
b,c=eval(input())
a[b],a[c]=a[c],a[b]
print(a)
