def count_foreign(ids):
    for i in ids:
        a=0
        if len(i)==9:
            a+=1
        else:
            pass
    return a
            

origin=input().split()
print(count_foreign(origin))

