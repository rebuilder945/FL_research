a = eval(input())
a.sort()
b = []
for i in a:
    if a.count(i)==1:
        b.append(str(i))
if len(b)==0:
    print('False')
else:
    print(','.join(b))
