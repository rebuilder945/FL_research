def count_foreign(ids):
    a=0
    ids.split()
    for i in ids:
        if i[0]=="L":
            a+=1


origin=input().split()
print(count_foreign(origin))

