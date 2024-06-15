lst = input().split()
n,m = input().split()
n = int(n)
m = int(m)
s = lst[n]
lst[n] = lst[m]
lst[m] = s
print(lst)


