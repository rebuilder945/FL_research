def count_foreign(ids):
    n=0
    for i in origin:
        if i[0]=="L":
            d=d+1
        else:
            d=0
        return d

origin=input().split()
print(count_foreign(origin))

