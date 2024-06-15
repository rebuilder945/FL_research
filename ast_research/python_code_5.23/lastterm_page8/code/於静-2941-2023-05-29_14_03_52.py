def count_foreign(ids):
    x=0
        for i in ids:
            if i.isalpha():
                x+=1
        return x

origin=input().split()
print(count_foreign(origin))

