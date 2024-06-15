a = list(input())
a[0],a[-1] = a[-1],a[0]
a[-2],a[1] = a[1],a[-2]
b = ''
for i in a:
    b += str(int(i)+5%10)
print(b)
