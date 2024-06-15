s = input() or 'None'
d = dict([])
if s != 'None':
    for i in s:
        d[i] = s.count(i)
    for k,v in d.items():
        if v == 1:
            break
    print(k)
else:
    print('None')
