def count_foreign(ids):
    x=0
    for str in ids:
        if len(str)=9:
            x+=1
    return x

origin=input().split()
print(count_foreign(origin))

