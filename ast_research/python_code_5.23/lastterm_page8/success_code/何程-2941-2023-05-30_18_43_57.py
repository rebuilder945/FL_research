def count_foreign(ids):
    for i in ids:
      if i[0]=="L":
        jishu+=1
    return jishu

origin=input().split()
print(count_foreign(origin))

