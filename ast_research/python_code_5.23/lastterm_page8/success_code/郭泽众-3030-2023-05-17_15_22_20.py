nlist = input().split(',')
slist = input().split(',')
lgh = len(nlist)
plist = []
for i in range(0, lgh):
    plist.append([nlist[i],slist[i]])
plist.sort(key = lambda plist:plist[1])
print(plist)
