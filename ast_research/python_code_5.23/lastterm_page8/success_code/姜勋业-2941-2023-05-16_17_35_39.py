def count_foreign(ids):
    k=0
    for i in ids:
         if str(i)[0]=="L":
             k+=1


origin=input().split()
print(count_foreign(origin))

