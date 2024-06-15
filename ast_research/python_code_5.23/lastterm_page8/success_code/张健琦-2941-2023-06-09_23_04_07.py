def count_foreign(ids):
        sum=0
        for i in ids:
            if i.find('L',0,len(i))==0:
                sum+=1
            else:
                pass
        return int(sum)

origin=input().split()
print(count_foreign(origin))

