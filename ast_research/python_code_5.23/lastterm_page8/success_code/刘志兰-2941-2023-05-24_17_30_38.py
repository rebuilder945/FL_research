def count_foreign(ids):
    ids=map(str,input().split())
    for x in range(ids):
          counts=0
          if len(x)==9:
            counts+=1
    return counts

origin=input().split()
print(count_foreign(origin))

