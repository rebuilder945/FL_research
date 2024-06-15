def count_foreign(ids):
    m=0
    for x in ids:
      if x[0] ==L:
         m +=1
    return m

origin=input().split()
print(count_foreign(origin))

