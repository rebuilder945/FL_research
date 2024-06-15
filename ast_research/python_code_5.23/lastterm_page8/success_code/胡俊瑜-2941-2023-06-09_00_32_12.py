def count_foreign(ids):
    import re
    lst=[eval(x) for x in ids]
    for i in lst:
        a=0
        if bool(re.search(L,str(i)))==True:
            a+=1
        else:
            pass
    return a
            

origin=input().split()
print(count_foreign(origin))

