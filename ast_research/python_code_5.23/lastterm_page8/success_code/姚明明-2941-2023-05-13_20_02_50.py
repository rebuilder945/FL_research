def count_foreign(ids):
    n=0
    for x in ids:
        if type(x) !=int:
            n+=1
    return n


origin=input().split()
print(count_foreign(origin))

