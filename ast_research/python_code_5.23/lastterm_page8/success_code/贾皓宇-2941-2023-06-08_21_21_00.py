def count_foreign(ids):
        for x in ids:
            s=0
            if x[0]=='L':
                s=s+1
        return s

origin=input().split()
print(count_foreign(origin))

