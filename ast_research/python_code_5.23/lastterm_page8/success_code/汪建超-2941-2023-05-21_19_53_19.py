def count_foreign(ids):
    lst = []
    for x in ids:
        if ids[1] in "L":
            lst.append(x)
    return len(lst)

origin=input().split()
print(count_foreign(origin))

