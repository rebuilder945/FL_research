istr = input()
plist = [x for x in istr]
tlist = []
for i in plist:
    lnum = ord(i)
    if 65 <= lnum <= 90:
        j = 155 - lnum
        tlist.append(chr(j))
    elif 97 <= lnum <= 122:
        j = 219 - lnum
        tlist.append(chr(j))
    else:
        tlist.append(i)
print(istr)
print(''.join(tlist))
