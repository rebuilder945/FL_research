n = int(input())
m = list(range(1,n+1,1))
a = []
b = []
for x in m:
    if x==1:
        a.append(x)
    else:
        b.append(x)
z = b+a
print(z)
