def count_foreign(ids):
    num=0
    for i in ids:
        if len(i)==9:
            num+=1
    return num

origin=input().split()
print(count_foreign(origin))

