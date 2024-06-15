def count_foreign(ids):
    s=0
    for i in ids:
        if len(i)==9:
            s+=1
        else:
            pass
    return s

origin=input().split()
print(count_foreign(origin))

