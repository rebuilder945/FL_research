def count_foreign(ids):
    lst=[]
    for i in origin:
        if i[0]=="L":
            lst.append(i)
    return len(lst)
            

origin=input().split()
print(count_foreign(origin))

