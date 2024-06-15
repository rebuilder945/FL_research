def count_foreign(ids):
         jishu=0
        for x in ids:
            if x[0]=='L':
                jishu+=1
        return jishu

origin=input().split()
print(count_foreign(origin))

