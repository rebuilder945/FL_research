def count_foreign(ids):
    num = 0
    if ids[0] == L:
        num+=1
    else:
        return 0
    return num


origin=input().split()
print(count_foreign(origin))

