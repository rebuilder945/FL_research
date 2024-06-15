def count_foreign(ids):
    num=0
    for x in ids:
        if str(x).startwith("L"):
            num+=1
    return num


origin=input().split()
print(count_foreign(origin))

