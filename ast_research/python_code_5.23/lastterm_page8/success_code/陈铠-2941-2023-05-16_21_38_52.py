def count_foreign(ids):
    a=0
    for x in ids:
        if ids[1]=="L":
            a+=1
    return a
        
        

origin=input().split()
print(count_foreign(origin))

