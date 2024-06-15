def count_foreign(ids):
    a=0
    for i in ids:
        b=eval(i)
        if str(b)[0]=="L":
            a+=1
        else:
            continue
    return a

origin=input().split()
print(count_foreign(origin))

