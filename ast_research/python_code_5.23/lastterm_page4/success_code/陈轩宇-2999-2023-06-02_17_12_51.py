a = (input()).split()
a = list(a)
fuck = (input()).split()
n,m = int(fuck[0]),int(fuck[1])
b = a[n]
c = a[m]
a[n] = c
a[m] = b
print(a)

