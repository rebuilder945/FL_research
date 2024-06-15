def count_foreign(ids):
    num=0
    for x in ids:
        if x[0]=="L":
            num=num+1
    return num

origin=input().split()
print(count_foreign(origin))

