def count_foreign(ids):
    counts=0
    for i in ids:
    if len(i)==9 and i[0]=='L':
    counts+=1
    return counts

origin=input().split()
print(count_foreign(origin))

