a = list(input().split())
n,m = input().split()
n1,m1 = int(n),int(m)
a[n1],a[m1] = a[m1],a[n1]
print(a)
