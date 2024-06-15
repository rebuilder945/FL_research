def count_foreign(ids):
    for x in ids:
        liuxuesheng=0
        if len(x)>8:
            liuxuesheng+=1
    return liuxuesheng
            

origin=input().split()
print(count_foreign(origin))

