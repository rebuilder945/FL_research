a = input()
c = ''
for i in a:
    if a.count(i) == 1:
        c += i
if c == '':
    print('None')
else:
    print(c)
