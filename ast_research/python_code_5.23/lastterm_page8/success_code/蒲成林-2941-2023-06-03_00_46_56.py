def count_foreign(ids):
            liu=0
            for x in ids:
                    if str(x)[0]=='L':
                            liu+=1
                    continue
            return liu

origin=input().split()
print(count_foreign(origin))

