a=input().split(' ')
c=input().split(' ')
b=a.copy()
b[int(c[0])]=a[int(c[1])]
b[int(c[1])]=a[int(c[0])]
print(b)


