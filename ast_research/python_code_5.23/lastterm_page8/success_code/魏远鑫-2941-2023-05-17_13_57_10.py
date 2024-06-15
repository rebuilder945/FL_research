def count_foreign(ids):
    for x in ids:
        a=0
        if len(x)==9:
            a+=1
    return a

origin=input().split()
print(count_foreign(origin))

