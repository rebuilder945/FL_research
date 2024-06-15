def count_foreign(ids):
        t = 0
        for x in ids:
            if x[0]=="L":
                t+=1
        return(t)

origin=input().split()
print(count_foreign(origin))

