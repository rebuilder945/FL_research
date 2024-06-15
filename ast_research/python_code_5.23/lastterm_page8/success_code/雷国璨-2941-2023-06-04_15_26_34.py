def count_foreign(ids):
    a=[]
    for i in ids:
        if i[0]=='L':
            a.append(i)
    else:
        pass
    return len(a)


origin=input().split()
print(count_foreign(origin))

