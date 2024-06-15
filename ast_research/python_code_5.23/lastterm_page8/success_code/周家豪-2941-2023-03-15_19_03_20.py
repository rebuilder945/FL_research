def count_foreign(ids):
        total=0
        for x in ids:
            if "L" in x:
                total+=1
        return total

origin=input().split()
print(count_foreign(origin))

