def count_foreign(ids):
    for i in range(len (ids)):
        a = 0
        if ids[i][0] == 'L':
            a = a + 1
    return a

origin=input().split()
print(count_foreign(origin))

