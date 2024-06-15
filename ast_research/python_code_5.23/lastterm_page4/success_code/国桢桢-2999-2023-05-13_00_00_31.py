l = input().split()
l2 =input().split()
n = l2[0]
m = l2[1]
a = l[n]
b = l[m]
l[n] = b
l[m] = a
print(l)
