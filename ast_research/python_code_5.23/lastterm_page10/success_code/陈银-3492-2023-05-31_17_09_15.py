a = input()
if a == '':
    print("None")
else:
    b = []
    for x in a:
        c=a.count(x)
        if c == 1:
            b.append(x)
    print(b[0])
