def count_foreign(ids):
        n=0
        for x in ids:
            if x[0]=='L':
                n+=1
        return n

origin=input().split()
print(count_foreign(origin))

