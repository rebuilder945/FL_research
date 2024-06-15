def count_foreign(ids):
    a = 0
        for i in ids:
            if i[0] == 'L':
                a += 1
            else:
                continue

origin=input().split()
print(count_foreign(origin))

