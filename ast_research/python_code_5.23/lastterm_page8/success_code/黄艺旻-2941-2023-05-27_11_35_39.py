def count_foreign(ids):
    a=0
    for i in range(len(ids)):
            if len(ids(i))==2:
                a+=1
                return a
            else:
                return 0


origin=input().split()
print(count_foreign(origin))

