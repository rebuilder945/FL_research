l = {}
s = input()
while s != 'q':
    l[s] = l.get(s,0) + 1
    s = input()
print(max(l,key = l.get),end = ' ')
print(max(l.values()))
