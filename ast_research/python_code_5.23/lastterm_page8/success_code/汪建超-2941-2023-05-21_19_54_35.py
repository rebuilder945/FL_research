def count_foreign(ids):
    lst = []
    for x in ids:
        if 'L' in x :
            lst.append(x)
    return len(lst)

origin=input().split()
print(count_foreign(origin))

