def count_foreign(ids):
    num=0
    for i in ids:
        if i[0]==L:
            num+=1
    return num

origin=input().split()
print(count_foreign(origin))

