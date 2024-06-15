def count_foreign(ids):
    count1=0
    for i in origin:
        if str(i)[0]=="L":
            count1+=1
    return count1


origin=input().split()
print(count_foreign(origin))

