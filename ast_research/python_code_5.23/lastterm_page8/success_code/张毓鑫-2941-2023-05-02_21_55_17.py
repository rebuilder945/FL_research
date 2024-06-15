def count_foreign(ids):
    a=0
    for i in ids:
        for x in i:
            if x=="L":
                a+=1
    return a

origin=input().split()
print(count_foreign(origin))

