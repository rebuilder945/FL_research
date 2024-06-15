def count_foreign(ids):
        if ids[0] != L:
            return 0
        else:
            return 1
            count_foreign(ids) += 1

origin=input().split()
print(count_foreign(origin))

