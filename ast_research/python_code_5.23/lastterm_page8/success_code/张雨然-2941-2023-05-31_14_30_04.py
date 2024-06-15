def count_foreign(ids):
    m=[x for x in ids]
    lst=[]
    for i in m:
        if i[0] in ['L']:
            lst=lst.append(i)
    num=len(lst)
    return num

origin=input().split()
print(count_foreign(origin))

