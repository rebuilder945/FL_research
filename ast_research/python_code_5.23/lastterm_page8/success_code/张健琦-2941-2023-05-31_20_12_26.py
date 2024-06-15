def count_foreign(ids):
        sum=0
        for i in ids:
            if len(i) == 9:
                sum += 1
        return int(sum)

origin=input().split()
print(count_foreign(origin))

