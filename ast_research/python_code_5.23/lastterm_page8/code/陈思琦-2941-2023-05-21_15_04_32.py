def count_foreign(ids):
    x=0
    for x in ids:
        if x[0]=='L':
            x+=1
    retrun x

origin=input().split()
print(count_foreign(origin))

