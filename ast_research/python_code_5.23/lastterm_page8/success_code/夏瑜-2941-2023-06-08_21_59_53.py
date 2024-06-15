def count_foreign(ids):
    i=0
    for x in ids:
      if x.startwith('L'):
        i+=1
    return i

origin=input().split()
print(count_foreign(origin))

