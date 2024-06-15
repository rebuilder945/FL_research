def count_foreign(ids):
        acount = 0
        for i in ids:
            if i[0] == 'L':
                acount += 1
        return acount

origin=input().split()
print(count_foreign(origin))

