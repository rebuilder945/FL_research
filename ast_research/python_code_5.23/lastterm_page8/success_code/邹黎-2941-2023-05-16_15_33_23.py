def count_foreign(ids):
    geshu=0
    for x in ids:
        if x[0]=="L":
            geshu+=1
    return geshu

origin=input().split()
print(count_foreign(origin))

