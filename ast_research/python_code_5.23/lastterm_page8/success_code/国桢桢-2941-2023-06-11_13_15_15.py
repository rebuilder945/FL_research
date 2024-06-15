def count_foreign(ids):
    l =[]
    for i in ids:
     if i[0]=="L":
      l.append(i)
    return len(l)
      

origin=input().split()
print(count_foreign(origin))

