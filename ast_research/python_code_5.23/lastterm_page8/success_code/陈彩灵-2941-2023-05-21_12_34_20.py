def count_foreign(ids):
        count_f=0
        for x in origin:
            if x[0]=='L':
                count_f+=1
        return count_f

origin=input().split()
print(count_foreign(origin))

