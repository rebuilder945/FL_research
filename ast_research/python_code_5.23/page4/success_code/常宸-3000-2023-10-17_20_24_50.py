a = eval(input()).split()
b = eval(input()).split()
n,m = int(b[0]),int(b[1])
a[n],a[m] = a[m],a[n]
print(a)
