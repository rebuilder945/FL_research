def count_foreign(ids):
    a=0
    ids=list(ids)
    for x in ids:
        if x[1]=="L":
            a+=1
    return a
            

origin=input().split()
print(count_foreign(origin))

