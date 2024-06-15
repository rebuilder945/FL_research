def count_foreign(ids):
    counter=0
    for i in ids:
        string=str(i)
        if str(i)[0]=='L':
            counter+=1
    return counter

origin=input().split()
print(count_foreign(origin))

