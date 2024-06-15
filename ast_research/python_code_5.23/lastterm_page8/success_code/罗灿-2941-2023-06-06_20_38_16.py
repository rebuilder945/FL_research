def count_foreign(ids):
        Lstu=[]
        for x in ids:
            for y in x:
                if y=="L":
                    Lstu.append(x)
        return len(Lstu)

origin=input().split()
print(count_foreign(origin))

