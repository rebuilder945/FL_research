def count_foreign(ids):
    sums=0
    for x in ids:
      if  x[0]=="L":
            sums+=1
    return sums


origin=input().split()
print(count_foreign(origin))

