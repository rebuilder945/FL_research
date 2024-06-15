def count_foreign(ids):
    s=0
    for i in ids:
        if ids[0] in ['L']:
            s+=1
        else:
            pass
    return s

origin=input().split()
print(count_foreign(origin))

