a = input()
c = ''
for i in a:
    if a.count(i) == 1 and c == '':
        c += i
if c == '':
    print('None')
else:
    print(c)
