def count_foreign(ids):
    count=0
    for x in ids:
      if x.startwith('L'):
        count+=1
    return count
      

origin=input().split()
print(count_foreign(origin))

