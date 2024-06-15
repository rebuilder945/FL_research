def count_foreign(ids):
    num=0
    for x in ids:
        if x.startswith("L"):
            num+=1
    return num


origin=input().split()
print(count_foreign(origin))

