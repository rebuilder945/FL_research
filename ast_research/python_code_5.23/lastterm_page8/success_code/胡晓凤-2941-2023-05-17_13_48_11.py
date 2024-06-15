def count_foreign(ids):
        sum=0
        if ids[0] in"L":
            sum+=1
        return sum

origin=input().split()
print(count_foreign(origin))

