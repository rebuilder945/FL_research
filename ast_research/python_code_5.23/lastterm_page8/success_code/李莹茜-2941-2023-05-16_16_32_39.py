def count_foreign(ids):
        count=0
        for i in range(len(ids)):
            if ids[i][0]=='L':
                count+=1
        return count

origin=input().split()
print(count_foreign(origin))

