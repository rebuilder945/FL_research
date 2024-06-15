def count_foreign(ids):
    s=0
    ids=[eval(x) for x in origin]
    for i in ids:
        if ids[0] in ['L']:
            s+=1
    return count_foreign(ids)

origin=input().split()
print(count_foreign(origin))

