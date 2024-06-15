def count_foreign(ids):
    res=0
    for x in ids:
        if ids[0]=='L':
            res+=1
    return res

origin=input().split()
print(count_foreign(origin))

