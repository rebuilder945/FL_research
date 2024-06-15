def count_foreign(ids):
    n = 0
    for i in orign:
        if len(i) == 9:
            n += 1
    return n


origin=input().split()
print(count_foreign(origin))

