a = str(input())
a = list(map(int,a))
n = len(a)
b = []
for i in a:
    i = (i+5)%10
    b.append(i)
if n%2==1:
    m = (n-1)/2
    m = int(m)
    for x in range(0,m,1):
        c = b[n-1-x]
        b[n-1-x] = b[x]
        b[x] = c
else:
    m = n/2
    m = int(m)
    for y in range(0,m,1):
        c = b[n-1-y]
        b[n-1-y] = b[y]
        b[y] = c
r = ""
for p in b:
    r = r + str(p)
print(r)

