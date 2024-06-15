def count_foreign(ids):
    i=0
    for x in ids:
         if len(x)==9:
              i+=1
         else:
              pass
    return i

origin=input().split()
print(count_foreign(origin))

