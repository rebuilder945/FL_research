def count_foreign(ids):
    jishu=0
        for x in ids:
            if len(x)==9:
                jishu+=1
            else:
                jishu=0
        return jishu

origin=input().split()
print(count_foreign(origin))

