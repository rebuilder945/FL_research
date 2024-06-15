a=eval(input())
a.sort()
b=len(a)
c=0
for x in range(b):
    c+=a[x]*(10**x)
print(c)
