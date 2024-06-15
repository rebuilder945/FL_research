def count_foreign(ids):
    count = 0
    for id in ids:
        if id[0] == 'L':
            count +=1
    return count

origin=input().split()
print(count_foreign(origin))

