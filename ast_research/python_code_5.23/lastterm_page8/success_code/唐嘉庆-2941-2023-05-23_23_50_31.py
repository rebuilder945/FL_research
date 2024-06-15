def count_foreign(ids):
    for i in ids:
        sum=0
        if len(i)== 9:
            sum+=1
    return int(sum)

origin=input().split()
print(count_foreign(origin))

