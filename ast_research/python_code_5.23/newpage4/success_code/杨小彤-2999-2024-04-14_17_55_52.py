a = str(input()).split()
n,m = list(int(x) for x in input('').split())
if n>len(a)-1:
    print("error")
elif m>len(a)-1:
    print("error")
else:
    c = a[n]
    a[n] = a[m]
    a[m] = c
print(a)
