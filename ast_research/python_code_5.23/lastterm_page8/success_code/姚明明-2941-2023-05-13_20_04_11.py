def count_foreign(ids):
    n=0
    for x in ids:
        if len(x) ==9:
            n+=1
    return n


origin=input().split()
print(count_foreign(origin))

