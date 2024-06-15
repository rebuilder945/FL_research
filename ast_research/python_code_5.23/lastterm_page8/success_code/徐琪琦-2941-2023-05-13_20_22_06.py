def count_foreign(ids):
    s = 0
    for i in ids:
        if i.startswith("L"):
            s += 1
    return s

origin=input().split()
print(count_foreign(origin))

