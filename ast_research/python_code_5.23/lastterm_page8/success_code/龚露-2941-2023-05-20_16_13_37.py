def count_foreign(ids):
    num=[]
    for x in ids:
        if x[0]=='L':
            num.append(x)
    c=len(num)
    return c

origin=input().split()
print(count_foreign(origin))

