def count_foreign(ids):
        sum=0
        for i in ids:
            if i[0]=="L":
                sum+=1
        return int(sum)


origin=input().split()
print(count_foreign(origin))

