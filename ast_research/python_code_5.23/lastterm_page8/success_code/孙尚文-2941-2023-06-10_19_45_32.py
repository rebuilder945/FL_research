def count_foreign(ids):
    a=0
    for i in ids:
        if str(i).startwith("L"):
            a+=1
    return a

origin=input().split()
print(count_foreign(origin))

