def count_foreign(ids):
    m=0
    for i in ids:
        if i[:1]=="L":
            m+=1
    return m

origin=input().split()
print(count_foreign(origin))

