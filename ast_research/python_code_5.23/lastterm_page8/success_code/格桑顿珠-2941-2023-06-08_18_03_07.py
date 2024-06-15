def count_foreign(ids):
        iCount = 0
        for x in ids:
            a = str(x)
            if a[0] == "L":
                iCount += 1
            else:
                pass
        return iCount

origin=input().split()
print(count_foreign(origin))

