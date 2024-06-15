def count_foreign(ids):
    str.count=0
        for i in ids:
            if i.isalpha():
                str.count+=1
        return str.count

origin=input().split()
print(count_foreign(origin))

