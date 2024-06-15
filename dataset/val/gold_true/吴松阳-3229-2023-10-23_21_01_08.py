a = eval(input())
a.sort(reverse = False)
if a.count(min(a, key = a.count)) == 1:
    b = []
    for i in a:
        if a.count(i) == 1:
            b.append(i)
    c = ''
    for x in range(len(b)):
        if x < len(b)-1:
            c += str(b[x]) + ','
        else:
            c += str(b[x])
    print(c)
else:
    print('False')
