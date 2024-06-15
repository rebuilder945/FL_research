def count_foreign(ids):
        lst=[0]
        for i in origin:
            if i.startswith("L"):
                lst.append(1)
        return sum(lst)

origin=input().split()
print(count_foreign(origin))

