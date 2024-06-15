a = input()
ls = []
c = ''
for i in a:
    if i.isnumeric():
        c += i
    else:
        ls.append(c)
        c = ''
ls.reverse()
d = 0
for i in ls:
    if d <= len(i):
        d = i
for i in ls:
    if len(i) == d:
        print(i)
        break




