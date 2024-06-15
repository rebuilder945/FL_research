def count_foreign(ids):
    for i in ids:
           if type(i[0])!=int:
                a+=1
                return a
        else:
            return 0

origin=input().split()
print(count_foreign(origin))

