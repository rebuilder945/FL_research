a = input().split()
b = input().split()
for x in range(len(a)):
    if a[x] in b:
        a.remove(a[x])
        a.insert(x,' ')
for i in a:
    print(i,end = ' ')


