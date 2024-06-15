def count_foreign(ids):
    count = 0
        for id in ids:
            if len(id) == 9 and id[0] == 'L':
                count += 1
        return count

origin=input().split()
print(count_foreign(origin))

