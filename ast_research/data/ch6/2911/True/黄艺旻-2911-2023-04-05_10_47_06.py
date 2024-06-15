a = list(input())
if len(a) == 2:
    a[0],a[-1] = a[-1],a[0]
else:
    a[-2],a[1] = a[1],a[-2]
    a[0],a[-1] = a[-1],a[0]
b = ''
for i in a:
    b += str((int(i)+5)%10)
print(b)
