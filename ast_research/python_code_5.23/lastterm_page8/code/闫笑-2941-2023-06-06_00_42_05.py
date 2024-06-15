def count_foreign(ids):
    num = 0
    for x in ids:
         if "L" in x:
            num+=1
         else:
            return 0
        return num


origin=input().split()
print(count_foreign(origin))

