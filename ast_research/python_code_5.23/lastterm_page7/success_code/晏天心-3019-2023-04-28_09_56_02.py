n,e,p,m = input().split()
e = int(e)
p = int(p)
m = int(m)
a = (e+p+m) / 3
ls = [e,p,m]
ls.sort(reverse = True)
print(n,f"{ls[0]:.2f} {ls[1]:.2f} {ls[2]:.2f} {a:.2f}")

