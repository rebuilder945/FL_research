a = list(map(str,input()))
for x in range(len(a)):
    a[x]=str((int(a[x])+5)%10)
a.reverse()
b = ''.join(a)
print(b)

