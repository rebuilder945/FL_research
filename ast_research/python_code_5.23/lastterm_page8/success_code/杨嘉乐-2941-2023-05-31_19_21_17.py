def count_foreign(ids):
    for x in ids:
        sum=0
        if len(x)==9:
            sum+=1
    return sum

origin=input().split()
print(count_foreign(origin))

