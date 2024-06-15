def count_foreign(ids):
    qishi=0
    for i in ids:
        if i[0]=="L":
            qishi+=1
    return qishi


origin=input().split()
print(count_foreign(origin))

