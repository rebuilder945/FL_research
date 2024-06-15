s = list(input()) or "None"
n = []
if s != 'None':
    for x in s:
        n.append(s.count(x))
    print(s[n.index(1)])
else:
    print('None')
