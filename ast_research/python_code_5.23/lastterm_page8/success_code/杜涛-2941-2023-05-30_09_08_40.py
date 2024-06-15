def count_foreign(ids):
    a=0
    for i in ids:
        if ids[0]=='L' and len(i)==9:
            a+=1
    return a

origin=input().split()
print(count_foreign(origin))

