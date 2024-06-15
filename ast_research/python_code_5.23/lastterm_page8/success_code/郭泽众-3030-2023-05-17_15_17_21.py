nlist = input().split(',')
slist = input().split(',')
lgh = len(nlist)
plist = []
for i in range(0, lgh):
    plist.append([nlist[i],slist[i]])
print(plist)
