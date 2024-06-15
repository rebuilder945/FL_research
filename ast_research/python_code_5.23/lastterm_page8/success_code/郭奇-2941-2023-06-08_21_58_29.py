def count_foreign(ids):
    lst=[]
    for i in range(len(ids)):
        if ids[i][0]=='L':
            lst+=1
    return lst.items()

origin=input().split()
print(count_foreign(origin))

