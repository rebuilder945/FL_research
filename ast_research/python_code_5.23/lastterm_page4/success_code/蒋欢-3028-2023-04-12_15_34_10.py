n,m,l=eval(input())
ap=[n]
for i in range(m-1):
    p=ap[i]+l
    ap.append(p)
print(ap)
