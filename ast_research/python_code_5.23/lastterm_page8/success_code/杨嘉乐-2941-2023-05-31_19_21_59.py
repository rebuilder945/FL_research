def count_foreign(ids):
    for x in ids:
        sum=0
        if x.find(L)!=-1:
            sum+=1
    return sum

origin=input().split()
print(count_foreign(origin))

