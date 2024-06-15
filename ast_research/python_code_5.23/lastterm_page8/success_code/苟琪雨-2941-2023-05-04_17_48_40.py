def count_foreign(ids):
    n=0
    for i in ids:
        if i[1]==L:
            n+=1
    return n

origin=input().split()
print(count_foreign(origin))

