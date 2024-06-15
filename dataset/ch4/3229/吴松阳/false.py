a = eval(input())
a.sort(reverse = False)
if a.count(min(a, key = a.count)) == 1:
    b = []
    for i in a:
        if a.count(i) == 1:
            b.append(i)
    c = ''
    for x in b:
        c += str(x) + ','
    print(c)
else:
    print('False')
