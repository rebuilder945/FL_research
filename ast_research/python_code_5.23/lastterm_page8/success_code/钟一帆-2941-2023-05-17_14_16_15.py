def count_foreign(ids):
    d=0
    for i in ids:
        if 'L' in i:
            d+=1
    return d

origin=input().split()
print(count_foreign(origin))

