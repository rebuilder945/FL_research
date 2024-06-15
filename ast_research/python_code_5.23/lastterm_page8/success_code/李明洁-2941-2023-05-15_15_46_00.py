def count_foreign(ids):
        if ids[0] != "L":
            return count_foreign(ids)
        else:
            ids+=1
            

origin=input().split()
print(count_foreign(origin))

