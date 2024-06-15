def count_foreign(ids):
    sum=0
    for x in ids:
        if 'L' in x:
            sum+=1
    return sum

origin=input().split()
print(count_foreign(origin))

