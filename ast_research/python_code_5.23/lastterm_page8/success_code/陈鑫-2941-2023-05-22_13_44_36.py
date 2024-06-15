def count_foreign(ids):
    a=input().split()
    b=0
    for i in a:
        if i[0]=="L":
            b+=1
    return b

origin=input().split()
print(count_foreign(origin))

