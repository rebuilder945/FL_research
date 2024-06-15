def count_foreign(ids):
    ls=[]
    for x in ids:
        if x[0]=="L":
            ls.append(x)
    return len(ls)

origin=input().split()
print(count_foreign(origin))

