def count_foreign(ids):
    a = 0
    for x in ids:
        if x[0] == 'L':
            a += 1
        else:
            a = a
    return a

origin=input().split()
print(count_foreign(origin))

