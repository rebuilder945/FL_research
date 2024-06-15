def count_foreign(ids):
    k=0
        for i in ids:
            if i[0]=="L":
                k+=1
        return k  

origin=input().split()
print(count_foreign(origin))

