def count_foreign(ids):
    b=0
    for i in origin:
        if i[0]=="L":
            b+=1
    return b

origin=input().split()
print(count_foreign(origin))

