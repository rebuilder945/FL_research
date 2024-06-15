def count_foreign(ids):
    lst=[]
    for i in ids:
        if i[0] in ['L']:
            lst=lst.append(i)
    num=len(lst)
    return num

origin=input().split()
print(count_foreign(origin))

