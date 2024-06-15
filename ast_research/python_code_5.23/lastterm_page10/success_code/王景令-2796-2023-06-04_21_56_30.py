a = input()
ls = []
c = ''
for i in a + 'a':
    if i.isnumeric():
        c += i
    else:
        if c != '':
            ls.append(c)
            c = ''
if len(ls) == 0:
    print('No digits')
ls.reverse()
d = 0
for i in ls:
    if d <= len(i):
        d = len(i)
for i in ls:
    if len(i) == d:
        print(i)
        break




