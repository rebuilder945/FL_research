def count_foreign(ids):
    for x in range(len(list(ids))):
          counts=0
          if len(x)==9:
            counts+=1
    return counts

origin=input().split()
print(count_foreign(origin))

