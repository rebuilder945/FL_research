def count_foreign(ids):
    a=0
    for i in range(len(ids)):
     if len(ids[i])==9:
      a+=1
    return a

origin=input().split()
print(count_foreign(origin))

