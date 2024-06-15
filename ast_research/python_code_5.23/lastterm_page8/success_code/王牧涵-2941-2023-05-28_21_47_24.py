def count_foreign(ids):
        origin=0
        for x in ids:
            if len(x)==9:
                origin+=1
                return origin


origin=input().split()
print(count_foreign(origin))

