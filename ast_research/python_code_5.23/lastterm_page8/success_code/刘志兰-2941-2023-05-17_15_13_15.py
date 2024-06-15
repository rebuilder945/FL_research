def count_foreign(ids):
    for x in ids:
          if len(x)==9:
             num+=1
    return num

origin=input().split()
print(count_foreign(origin))

