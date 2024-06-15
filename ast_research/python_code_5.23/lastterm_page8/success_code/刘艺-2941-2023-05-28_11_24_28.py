def count_foreign(ids):
        ls = ['1','2','3','4','5','6','7','8','9','0']
        a = 0
        for x in ids:
            if x[0] in ls:
                pass
            else:
                a += 1
        return a

origin=input().split()
print(count_foreign(origin))

