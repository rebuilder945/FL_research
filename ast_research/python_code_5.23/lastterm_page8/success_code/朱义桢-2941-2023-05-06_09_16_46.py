def count_foreign(ids):
        a=0
        for x in ids:
            if x.startswith("L"):
                a+=1
            else:
                pass
        return(a)

origin=input().split()
print(count_foreign(origin))

