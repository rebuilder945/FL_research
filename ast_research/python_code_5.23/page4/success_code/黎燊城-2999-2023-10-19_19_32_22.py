l=list(input().split())
n,m=(input().split())
n = int(n)
m = int(m)
l[n],l[m]=l[m],l[n]
print(l)
