def count_foreign(ids):
    for x in ids:
        liuxuesheng=0
        for i in x:
            if i =="L":
                liuxuesheng+=1
    return liuxuesheng
            

origin=input().split()
print(count_foreign(origin))

