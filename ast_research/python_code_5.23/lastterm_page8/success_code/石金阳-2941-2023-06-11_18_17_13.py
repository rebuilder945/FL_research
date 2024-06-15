def count_foreign(ids):
    a=0
    for i in range(len(ids)-1):
            if ids[i][0]=='L':
                    a+=1
    return a

origin=input().split()
print(count_foreign(origin))

