s=input()
a=s.split()
b,c=eval(input())
d=a[b]
a[b]=a[c]
a[c]=d
print(a)
