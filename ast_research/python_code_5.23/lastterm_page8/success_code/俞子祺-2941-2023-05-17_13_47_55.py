def count_foreign(ids):
    liuxuesheng=0
    for x in ids:
        if x[0]=="L":
            liuxuesheng+=1
    return liuxuesheng
            

origin=input().split()
print(count_foreign(origin))

