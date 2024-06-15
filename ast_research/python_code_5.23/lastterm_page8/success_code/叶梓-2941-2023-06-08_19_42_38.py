def count_foreign(ids):
    nums=0
    for x in ids:
        if len(x)==9:
            nums+=1
        else:
            nums=nums

origin=input().split()
print(count_foreign(origin))

