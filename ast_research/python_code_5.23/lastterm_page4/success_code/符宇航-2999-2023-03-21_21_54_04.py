lst = input().split()
n,m = input().split()
n = int(n)
m = int(m)
x = lst[n]
y = lst[m]
lst[n] = y
lst[m] = x
print(lst)

