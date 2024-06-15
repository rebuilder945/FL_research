istr = input()
if len(istr) == 0:
    print('None')
plist = [x for x in istr]
ulist = []
for i in plist:
    if plist.count(i) == 1:
        ulist.append(i)
print(ulist[0])
