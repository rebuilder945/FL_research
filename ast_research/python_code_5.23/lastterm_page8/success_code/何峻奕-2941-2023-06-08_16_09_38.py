def count_foreign(ids):
    d=0
    for i in origin:
        if i[0]=="L":
            d=d+1
        else:
            d=d
    return d

origin=input().split()
print(count_foreign(origin))

