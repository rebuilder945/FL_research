def count_foreign(ids):
        sum=0
        for ids in origin:
            if ids[0] in"L":
                sum+=1
        return sum

origin=input().split()
print(count_foreign(origin))

