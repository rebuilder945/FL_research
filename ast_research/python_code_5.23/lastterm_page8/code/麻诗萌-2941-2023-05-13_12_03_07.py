def count_foreign(ids):
    s=0
    for x in ids:
        if len(x)==9：
            s+=1
    return s

origin=input().split()
print(count_foreign(origin))

