a = input()
if not a :
    print('None')
else:
    found = False
    for x in a :
        if a.count(x) == 1:
            print(x)
            found = Ture
            break

    if not found:
        print('None')
