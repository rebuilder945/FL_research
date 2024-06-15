def count_foreign(ids):
    for i in ids:
            a=0
            if type(i[0])!=type(1):
                a+=1
                return a

origin=input().split()
print(count_foreign(origin))

