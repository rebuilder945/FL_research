def count_foreign(ids):
    a=0
    for i in ids:
            if len(i)==9:
                a+=1
            return a
            else:
                return 0

origin=input().split()
print(count_foreign(origin))

