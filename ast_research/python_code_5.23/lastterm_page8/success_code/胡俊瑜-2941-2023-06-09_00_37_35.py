def count_foreign(ids):
    lst=[eval(x) for x in ids]
    for i in lst:
        a=0
        if len(i)==9:
            a+=1
        else:
            pass
    return a
            

origin=input().split()
print(count_foreign(origin))

