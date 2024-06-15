def count_foreign(ids):
        jishu=0
        for i in ids:
            if i.startswith("L"):
                jishu+=1
        return jishu

origin=input().split()
print(count_foreign(origin))

