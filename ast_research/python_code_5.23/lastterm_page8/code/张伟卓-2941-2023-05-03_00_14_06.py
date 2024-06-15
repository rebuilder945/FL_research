def count_foreign(ids):
    for i in ids:
        n=0
        if "L" in i:
        n+=1
    return(n)

origin=input().split()
print(count_foreign(origin))

