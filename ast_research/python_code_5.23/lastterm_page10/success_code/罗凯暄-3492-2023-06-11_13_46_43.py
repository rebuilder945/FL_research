
s = input()
if not s:
    print("None")
else:
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    for c in s:
        if d[c] == 1:
            print(c)
            break


