a = eval(input())
if a.count(max(a, key = a.count)) > 1:
    b = []
    for i in a:
        if i not in b:
            b.append(i)
    print(b)
else:
    print('False')
