def count_foreign(ids):
    i=0
        i=0
        for x in ids:
            if x[0]=="L":
                i+=1
            else:
                pass
        return i

origin=input().split()
print(count_foreign(origin))

