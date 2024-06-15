def count_foreign(ids):
    l=0
    for x in ids:
        if x[0]=="L":
            l+=1
    return l


origin=input().split()
print(count_foreign(origin))

