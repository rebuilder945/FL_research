def count_foreign(ids):
    count_foreign = 0
    for i in range(1,2):
        if i.isalpha():
            count_foreign += 1
        else:
            pass

origin=input().split()
print(count_foreign(origin))

