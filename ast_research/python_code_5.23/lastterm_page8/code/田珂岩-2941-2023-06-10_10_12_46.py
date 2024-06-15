def count_foreign(ids):
    ls = list(ids)
    for x in ls;
        if x[0] == 'L' and len(x) == 9:
            return True


origin=input().split()
print(count_foreign(origin))

