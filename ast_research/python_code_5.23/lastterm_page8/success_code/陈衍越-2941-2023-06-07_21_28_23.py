def count_foreign(ids):
    lxs=0
    for i in ids:
        if i[0]=='L':
            lxs=lxs+1
    return lxs
            

origin=input().split()
print(count_foreign(origin))

