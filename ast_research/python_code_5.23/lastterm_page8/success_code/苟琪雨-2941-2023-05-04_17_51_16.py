def count_foreign(ids):
    n=0
    for i in range(len(ids)):
        if ids[i][1]=='L':
            n+=1
    return n

origin=input().split()
print(count_foreign(origin))

