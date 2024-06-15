def count_foreign(ids):
    lst=[0]
    for i in range(len(ids)):
        if ids[i][0]=='L':
            lst[0]+=1
    for x in lst:
        return x

origin=input().split()
print(count_foreign(origin))

