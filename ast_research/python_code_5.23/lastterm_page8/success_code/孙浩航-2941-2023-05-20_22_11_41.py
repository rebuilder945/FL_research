def count_foreign(ids):
        a=0
        for x in origin:
            if x[0]=="L":
                a=a+1
        return a

origin=input().split()
print(count_foreign(origin))

