def count_foreign(ids):
    count=0
    for i in ids:
        if len(i)==9:
            count+=1
    return count

origin=input().split()
print(count_foreign(origin))

