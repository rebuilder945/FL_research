a=input()
c,d=list(map(int,input().strip().split()))
a=a.split()
a[c],a[d]=a[d],a[c]
print(a)

