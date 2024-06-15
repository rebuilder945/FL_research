a = input().split(',')
b = input().split(',')
c = []
for i in range(len(a)):
    c.append([a[i],int(b[i])])
c.sort(key=lambda x:x[1])
print (c)
