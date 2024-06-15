def count_foreign(ids):
    for x in ids:
         sums=0
         if len(x)==9 :
            sums+=1
    return sums


origin=input().split()
print(count_foreign(origin))

