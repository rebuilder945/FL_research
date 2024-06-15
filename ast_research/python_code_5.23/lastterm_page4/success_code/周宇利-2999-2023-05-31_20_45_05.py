a=list(input(),split())
b,c=eval(input())
m=a[b]
a[b]=a[c]
a[c]=m
print(a)
