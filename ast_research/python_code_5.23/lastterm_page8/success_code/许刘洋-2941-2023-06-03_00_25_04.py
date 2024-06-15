def count_foreign(ids):
    a=list(ids)
    return a.count('L')

origin=input().split()
print(count_foreign(origin))

