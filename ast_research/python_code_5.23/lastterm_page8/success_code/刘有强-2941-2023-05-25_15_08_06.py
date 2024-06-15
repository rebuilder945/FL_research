def count_foreign(ids):
        sums=0
        for x in list(ids):
            if x.startswith("L") and len(x) == 9:
                sums += 1
        return sums

origin=input().split()
print(count_foreign(origin))

