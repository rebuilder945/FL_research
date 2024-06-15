def count_foreign(ids):
    ls = list(ids)
    s = 0
    for x in ls:
        if x[0] == 'L' and len(x) == 9:
            s += 1
    return s


origin=input().split()
print(count_foreign(origin))

