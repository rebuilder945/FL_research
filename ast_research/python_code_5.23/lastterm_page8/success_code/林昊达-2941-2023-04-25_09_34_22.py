def count_foreign(ids):
    t=0
    for i in ids:
            if i[0]=="L":
                    t+=1
    return t

origin=input().split()
print(count_foreign(origin))

