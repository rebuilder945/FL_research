def count_foreign(ids):
    
        n=0    
        for i in ids:
            if "L" in i:
                n+=1
        return n

origin=input().split()
print(count_foreign(origin))

