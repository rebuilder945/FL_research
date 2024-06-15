def count_foreign(ids):
        origin=0
        for x in ids:
            while x[0]=="L":
                origin+=1
                return origin


origin=input().split()
print(count_foreign(origin))

